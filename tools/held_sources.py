#!/usr/bin/env python3
"""Build an index of locally held source files.

The index is intentionally conservative: a file enters the output only when it
exists locally, and its hash, size, kind and page count are measured from that
file.  Manifests, access records and the completion queue can attach source
identity metadata, but they do not override the live bytes.
"""

from __future__ import annotations

import argparse
import contextlib
import csv
import hashlib
import io
import json
import os
import re
import sys
import tempfile
import warnings
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Iterable, NamedTuple


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUT = ROOT / "spec/coverage/edition-2026/held-sources.json"
QUEUE = ROOT / "spec/coverage/edition-2026/completion-work-queue.jsonl"

WALK_EXTENSIONS = {
    ".pdf",
    ".djvu",
    ".epub",
    ".html",
    ".htm",
    ".txt",
    ".png",
    ".jpg",
    ".jpeg",
    ".tif",
    ".tiff",
    ".gif",
    ".webp",
    ".bmp",
}
NAMED_FILE_EXTENSIONS = WALK_EXTENSIONS | {".ps", ".body", ".dat"}
IMAGE_EXTENSIONS = {
    ".png",
    ".jpg",
    ".jpeg",
    ".tif",
    ".tiff",
    ".gif",
    ".webp",
    ".bmp",
}
PATHISH_KEYS = (
    "path",
    "file",
    "filename",
    "artifact",
    "capture",
    "pdf",
    "html",
    "txt",
    "text",
    "image",
    "render",
    "extraction",
)
SHA_RE = re.compile(r"^[A-Fa-f0-9]{64}$")
SOURCE_FILE_CONTAINER_KEYS = {
    "source_file",
    "source_files",
    "held_source_file",
    "held_source_files",
    "local_source_file",
    "local_source_files",
}


def ordered_add(values: list[str], seen: set[str], value: Any) -> None:
    if value is None:
        return
    if isinstance(value, (list, tuple)):
        for item in value:
            ordered_add(values, seen, item)
        return
    if not isinstance(value, str):
        value = str(value)
    value = value.strip()
    if value and value not in seen:
        values.append(value)
        seen.add(value)


@dataclass
class RecordMeta:
    source_ids: list[str] = field(default_factory=list)
    bibkeys: list[str] = field(default_factory=list)
    titles: list[str] = field(default_factory=list)
    versions: list[str] = field(default_factory=list)
    body_states: list[str] = field(default_factory=list)
    access_bases: list[str] = field(default_factory=list)
    extent_verified: list[bool] = field(default_factory=list)
    evidence: list[str] = field(default_factory=list)
    _source_ids_seen: set[str] = field(default_factory=set, repr=False)
    _bibkeys_seen: set[str] = field(default_factory=set, repr=False)
    _titles_seen: set[str] = field(default_factory=set, repr=False)
    _versions_seen: set[str] = field(default_factory=set, repr=False)
    _body_states_seen: set[str] = field(default_factory=set, repr=False)
    _access_bases_seen: set[str] = field(default_factory=set, repr=False)
    _evidence_seen: set[str] = field(default_factory=set, repr=False)

    def add_source_id(self, value: Any) -> None:
        ordered_add(self.source_ids, self._source_ids_seen, value)

    def add_bibkey(self, value: Any) -> None:
        ordered_add(self.bibkeys, self._bibkeys_seen, value)

    def add_title(self, value: Any) -> None:
        ordered_add(self.titles, self._titles_seen, value)

    def add_version(self, value: Any) -> None:
        ordered_add(self.versions, self._versions_seen, value)

    def add_body_state(self, value: Any) -> None:
        ordered_add(self.body_states, self._body_states_seen, value)

    def add_access_basis(self, value: Any) -> None:
        ordered_add(self.access_bases, self._access_bases_seen, value)

    def add_extent_verified(self, value: Any) -> None:
        if isinstance(value, bool) and value not in self.extent_verified:
            self.extent_verified.append(value)

    def add_evidence(self, value: str) -> None:
        ordered_add(self.evidence, self._evidence_seen, value)

    def merge(self, other: "RecordMeta") -> None:
        self.add_source_id(other.source_ids)
        self.add_bibkey(other.bibkeys)
        self.add_title(other.titles)
        self.add_version(other.versions)
        self.add_body_state(other.body_states)
        self.add_access_basis(other.access_bases)
        for item in other.extent_verified:
            self.add_extent_verified(item)
        for item in other.evidence:
            self.add_evidence(item)


@dataclass
class HeldRecord:
    path: str
    abs_path: Path
    meta: RecordMeta = field(default_factory=RecordMeta)
    sha256: str | None = None
    bytes: int | None = None
    kind: str | None = None
    pdf_pages: int | None = None

    def merge_meta(self, meta: RecordMeta) -> None:
        self.meta.merge(meta)


@dataclass
class BuildStats:
    missing_named_paths: list[str] = field(default_factory=list)
    sha_mismatches: list[str] = field(default_factory=list)
    unpaired_pins: list[str] = field(default_factory=list)
    unreadable_json: list[str] = field(default_factory=list)
    # field -> "<path>: <recorded values>" for each file whose records disagree.
    value_conflicts: dict[str, list[str]] = field(default_factory=dict)
    pdf_page_errors: int = 0


class HeldIndex:
    def __init__(self, root: Path) -> None:
        self.root = root.resolve()
        self.records: dict[str, HeldRecord] = {}
        self.stats = BuildStats()

    def relpath(self, path: Path) -> str:
        resolved = path.resolve()
        try:
            return resolved.relative_to(self.root).as_posix()
        except ValueError:
            return resolved.as_posix()

    def add_file(self, path: Path, meta: RecordMeta) -> HeldRecord:
        rel = self.relpath(path)
        record = self.records.get(rel)
        if record is None:
            record = HeldRecord(rel, path.resolve())
            self.records[rel] = record
        record.merge_meta(meta)
        return record


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig")


def read_json(path: Path) -> Any:
    return json.loads(read_text(path))


def stream_sha256(path: Path) -> tuple[str, int]:
    digest = hashlib.sha256()
    total = 0
    with path.open("rb") as handle:
        while True:
            chunk = handle.read(1024 * 1024)
            if not chunk:
                break
            digest.update(chunk)
            total += len(chunk)
    return digest.hexdigest(), total


def first_bytes(path: Path, size: int = 1024) -> bytes:
    with path.open("rb") as handle:
        return handle.read(size)


# Before `%PDF-`, an HTML/XML marker or a word means the header is not a PDF's.
PDF_PREFIX_BLOCKER = re.compile(rb"<|[A-Za-z]{3,}")


def kind_for(path: Path, header: bytes) -> str:
    """Kind from the file's first bytes; a .pdf name never makes a file a PDF.

    `%PDF-` counts at offset 0 or after leading binary or whitespace junk in
    the first 1024 bytes, never after an HTML marker or prose.
    """
    position = header[:1024].find(b"%PDF-")
    if position >= 0 and not PDF_PREFIX_BLOCKER.search(header[:position]):
        return "pdf"
    lowered = header.lstrip(b"\xef\xbb\xbf \t\r\n")[:128].lower()
    if b"<html" in lowered or b"<!doctype html" in lowered:
        return "html"
    suffix = path.suffix.lower()
    if suffix == ".pdf":
        return "other"
    if suffix in {".html", ".htm"}:
        return "html"
    if suffix in {".txt", ".md"}:
        return "txt"
    if suffix in IMAGE_EXTENSIONS:
        return "image"
    if header.startswith((b"\x89PNG\r\n\x1a\n", b"\xff\xd8\xff", b"GIF87a", b"GIF89a")):
        return "image"
    if header.startswith((b"II*\x00", b"MM\x00*")):
        return "image"
    return "other"


def pdf_page_count(path: Path) -> int | None:
    """Page count of a content-verified PDF; never parses another format.

    Library warnings and log output are swallowed: a PDF that neither library
    can count gets None.
    """
    with (
        warnings.catch_warnings(),
        contextlib.redirect_stderr(io.StringIO()),
        contextlib.redirect_stdout(io.StringIO()),
    ):
        warnings.simplefilter("ignore")
        try:
            import fitz  # type: ignore

            with fitz.open(str(path), filetype="pdf") as document:
                return int(document.page_count)
        except Exception:
            pass
        try:
            from pypdf import PdfReader  # type: ignore

            reader = PdfReader(str(path), strict=False)
            return int(len(reader.pages))
        except Exception:
            return None


def unique_or_null(values: list[str]) -> str | None:
    cleaned = [value for value in values if value]
    if len(cleaned) == 1:
        return cleaned[0]
    return None


def bool_unique_or_null(values: list[bool]) -> bool | None:
    if len(values) == 1:
        return values[0]
    return None


def location_stable_for(path: str) -> bool:
    return path.startswith("citations/") or path.startswith("source/references/")


def output_entry(record: HeldRecord) -> dict[str, Any]:
    return {
        "path": record.path,
        "sha256": record.sha256,
        "bytes": record.bytes,
        "kind": record.kind,
        "pdf_pages": record.pdf_pages,
        "source_ids": sorted(record.meta.source_ids),
        "bibkeys": sorted(record.meta.bibkeys),
        "titles": sorted(record.meta.titles),
        "version": unique_or_null(record.meta.versions),
        "extent_verified": bool_unique_or_null(record.meta.extent_verified),
        "body_state": unique_or_null(record.meta.body_states),
        "access_basis": unique_or_null(record.meta.access_bases),
        "evidence": sorted(record.meta.evidence),
        "location_stable": location_stable_for(record.path),
    }


def index_to_output(index: HeldIndex) -> dict[str, Any]:
    for record in index.records.values():
        if record.sha256 is None or record.bytes is None:
            record.sha256, record.bytes = stream_sha256(record.abs_path)
        if record.kind is None:
            header = first_bytes(record.abs_path)
            record.kind = kind_for(record.abs_path, header)
        if record.kind == "pdf" and record.pdf_pages is None:
            record.pdf_pages = pdf_page_count(record.abs_path)
            if record.pdf_pages is None:
                index.stats.pdf_page_errors += 1
        conflicts = (
            ("version", record.meta.versions),
            ("body_state", record.meta.body_states),
            ("access_basis", record.meta.access_bases),
            ("extent_verified", record.meta.extent_verified),
        )
        for name, values in conflicts:
            if len(values) > 1:
                index.stats.value_conflicts.setdefault(name, []).append(
                    f"{record.path}: {json.dumps(values, ensure_ascii=False)}"
                )

    entries = [output_entry(record) for record in index.records.values()]
    entries.sort(key=lambda item: item["path"])
    source_index: dict[str, list[str]] = {}
    for entry in entries:
        for source_id in entry["source_ids"]:
            source_index.setdefault(source_id, []).append(entry["path"])
    for paths in source_index.values():
        paths.sort()
    return {"entries": entries, "source_index": dict(sorted(source_index.items()))}


def clean_path_string(value: str) -> str:
    value = value.strip()
    value = value.strip("`'\"")
    value = value.rstrip(".,;:)")
    value = value.lstrip("(")
    return value.replace("\\", "/")


def looks_like_url(value: str) -> bool:
    lowered = value.lower()
    return "://" in lowered or lowered.startswith(("mailto:", "doi:"))


def is_under(path: Path, directory: Path) -> bool:
    try:
        path.resolve().relative_to(directory.resolve())
        return True
    except ValueError:
        return False


def candidate_paths(value: str, root: Path, base_dir: Path | None) -> list[Path]:
    text = clean_path_string(value)
    path = Path(text)
    if path.is_absolute():
        return [path]
    candidates: list[Path] = []
    if base_dir is not None:
        candidates.append(base_dir / text)
    candidates.append(root / text)
    return candidates


def is_indexable_held_file(path: Path, root: Path, allow_tmp: bool = False) -> bool:
    if path.suffix.lower() not in NAMED_FILE_EXTENSIONS:
        return False
    held_roots = [root / "citations", root / "source/references"]
    if allow_tmp:
        held_roots.append(root / "tmp")
    return any(is_under(path, held_root) for held_root in held_roots)


def could_be_indexable_missing_path(
    value: str,
    root: Path,
    base_dir: Path | None,
    allow_tmp: bool = False,
) -> bool:
    cleaned = clean_path_string(value)
    if not cleaned or looks_like_url(cleaned) or "\n" in cleaned:
        return False
    if Path(cleaned).suffix.lower() not in NAMED_FILE_EXTENSIONS:
        return False
    return any(
        is_indexable_held_file(candidate, root, allow_tmp)
        for candidate in candidate_paths(cleaned, root, base_dir)
    )


def resolve_named_path(value: Any, root: Path, base_dir: Path | None) -> Path | None:
    if not isinstance(value, str):
        return None
    text = clean_path_string(value)
    if not text or looks_like_url(text) or "\n" in text:
        return None
    for candidate in candidate_paths(text, root, base_dir):
        try:
            resolved = candidate.resolve()
        except OSError:
            continue
        if resolved.is_file():
            return resolved
    return None


def has_file_extension(value: str) -> bool:
    suffix = Path(clean_path_string(value)).suffix.lower()
    return suffix in NAMED_FILE_EXTENSIONS


def key_is_pathish(key: str) -> bool:
    lowered = key.lower()
    return any(part in lowered for part in PATHISH_KEYS)


MALFORMED_PIN = "malformed"
# Every (hash key, pin) recorded for one file; the file must match all of them.
Pins = tuple[tuple[str, str], ...]


def recorded_pin(value: Any) -> str | None:
    """A recorded sha256 as lowercase hex, None when absent, else MALFORMED_PIN.

    A `sha256:` or SRI-style `sha256-` prefix is accepted.  A boolean is a
    flag, not a pin.
    """
    if value is None or isinstance(value, bool):
        return None
    if isinstance(value, str):
        cleaned = value.strip()
        if cleaned.lower().startswith(("sha256:", "sha256-")):
            cleaned = cleaned[len("sha256:"):].strip()
        if SHA_RE.fullmatch(cleaned):
            return cleaned.lower()
    return MALFORMED_PIN


def pin_failure(path: Path, pins: Pins) -> str | None:
    """Why `path` fails one of its recorded pins, or None when it matches all."""
    for hash_key, pin in pins:
        if pin == MALFORMED_PIN:
            return f"recorded {hash_key} is not a single sha256 hex digest"
    actual_sha, _actual_bytes = stream_sha256(path)
    for hash_key, pin in pins:
        if pin != actual_sha:
            return f"recorded {hash_key} {pin} actual {actual_sha}"
    return None


# Keys whose value is the file that a sibling plain pin (PLAIN_SHA_KEYS)
# describes.  Any other pathish key also takes that pin when it is the only
# pathish key in the record that names a file (see sole_file_valued_key).
GENERIC_SHA_PATH_KEYS = {
    "path",
    "file",
    "filename",
    "file_path",
    "local_path",
    "local_file",
    "local_artifact",
    "local_artifacts",
    "artifact",
    "artifacts",
    "local_capture",
    "capture",
    "held_pdf",
    "local_pdf",
    "pdf",
    "pdf_path",
    "pdf_file",
}


def normal_key(key: Any) -> str:
    """Key name for pin matching: lower case, `-` read as `_`, `sha_256` as sha256."""
    return str(key).lower().replace("-", "_").replace("sha_256", "sha256")


def names_a_file(value: Any) -> bool:
    """True when a path value names a file: a file-like string, or a list or
    dict item holding one (a dict item under any pathish key)."""
    if isinstance(value, str):
        return not looks_like_url(clean_path_string(value)) and has_file_extension(value)
    if isinstance(value, list):
        return any(names_a_file(item) for item in value)
    if isinstance(value, dict):
        return any(key_is_pathish(key) and names_a_file(item) for key, item in value.items())
    return False


def sole_file_valued_key(key: str, context: dict[str, Any]) -> bool:
    file_keys = [
        actual_key
        for actual_key, actual_value in context.items()
        if key_is_pathish(actual_key) and names_a_file(actual_value)
    ]
    return file_keys == [key]


PLAIN_SHA_KEYS = ("sha256", "recorded_sha256", "file_sha256")
EACH_COPY_SHA_KEY = "sha256_each_copy"
# A nested dict under a key containing one of these is folded into sha_view.
HASH_CONTAINER_PARTS = ("hash", "checksum", "digest")
# Name parts that end a path key: `<stem>_<word>` pairs with `<stem>_sha256`.
PATH_WORDS = {
    "path",
    "paths",
    "file",
    "files",
    "filename",
    "artifact",
    "artifacts",
    "capture",
    "captures",
    "pdf",
    "html",
    "txt",
    "text",
    "image",
    "render",
    "extraction",
}
# Path keys whose file is another work or an auxiliary file, not the record's
# own source: such files are indexed with evidence but get no identity.
OTHER_ROLE_KEY_PARTS = (
    "dependency",
    "dependencies",
    "metadata",
    "failed_response",
    "contents",
)
IDENTITY_MARKER_KEYS = ("source_key", "source_id", "bibliographic_identity")


ALGORITHM_KEYS = ("algorithm", "algo", "hash_algorithm")
ALGORITHM_VALUE_KEYS = ("value", "digest", "hexdigest", "hex", "hash")


def algorithm_name(value: dict[str, Any]) -> str:
    """`sha256` for {"algorithm": "SHA-256"}; '' when the dict names no algorithm."""
    name = next((value[key] for key in ALGORITHM_KEYS if isinstance(value.get(key), str)), "")
    return normal_key(name).replace("_", "")


def algorithm_pin(value: Any) -> Any:
    """The recorded digest of an {"algorithm": "sha256", "value": ...} dict, else None."""
    if not isinstance(value, dict) or algorithm_name(value) != "sha256":
        return None
    return next(
        (value[key] for key in ALGORITHM_VALUE_KEYS if value.get(key) is not None), None
    )


def names_any_path(value: Any) -> bool:
    """True when a path value names a file of any type (`notes.md`, `a.pdf`)."""
    if isinstance(value, list):
        return any(names_any_path(item) for item in value)
    if not isinstance(value, str):
        return False
    cleaned = clean_path_string(value)
    return bool(cleaned) and not looks_like_url(cleaned) and bool(Path(cleaned).suffix)


def names_file_record(value: Any) -> bool:
    """True for a dict that names a file of any type under a pathish key: a
    record of its own, whose pins describe its files."""
    return isinstance(value, dict) and any(
        key_is_pathish(key) and (names_a_file(item) or names_any_path(item))
        for key, item in value.items()
    )


def sha_view(context: dict[str, Any]) -> dict[str, Any]:
    """Normalised keys of a record, with nested hash/checksum/digest dicts (or
    lists of such dicts naming no file) and algorithm/value pairs folded in.

    An algorithm/value pair under `key` reads as `<key>_sha256`.  Two different
    pins for one sha256 key make that key malformed.
    """
    view: dict[str, Any] = {}

    def put(key: Any, value: Any) -> None:
        name = normal_key(key)
        if "sha256" in name and name in view:
            old, new = recorded_pin(view[name]), recorded_pin(value)
            if new is None:
                return
            if old is not None and old != new:
                value = "conflicting recorded values"
        view[name] = value

    def put_pair(key: Any, pin: Any) -> None:
        name = normal_key(key)
        put(name if "sha256" in name else f"{name}_sha256", pin)

    for key, value in context.items():
        pair = algorithm_pin(value)
        if pair is not None:
            put_pair(key, pair)
            continue
        put(key, value)
        if not any(part in normal_key(key) for part in HASH_CONTAINER_PARTS):
            continue
        items = [value] if isinstance(value, dict) else value if isinstance(value, list) else []
        for item in items:
            if isinstance(value, list) and (not isinstance(item, dict) or names_file_record(item)):
                continue
            pair = algorithm_pin(item)
            if pair is not None:
                put_pair(key, pair)
                continue
            for inner_key, inner_value in item.items():
                put(inner_key, inner_value)
    return view


def file_keyed_pins(context: dict[str, Any]) -> list[tuple[str, str, str]]:
    """(label, file name, pin) for each sha256 digest keyed by a file name in a
    hash/checksum/digest dict, such as {"file_hashes": {"a.pdf": digest}} or
    {"hashes": {"a.pdf": {"sha256": digest}}}."""
    found: list[tuple[str, str, str]] = []
    for key, value in context.items():
        if not (
            isinstance(value, dict)
            and any(part in normal_key(key) for part in HASH_CONTAINER_PARTS)
        ):
            continue
        for inner_key, inner_value in value.items():
            if isinstance(inner_value, dict):
                inner_value = sha_view(inner_value).get("sha256")
            pin = recorded_pin(inner_value)
            if has_file_extension(str(inner_key)) and pin not in (None, MALFORMED_PIN):
                found.append((f"{key}[{inner_key}]", clean_path_string(str(inner_key)), pin))
    return found


def stem_sha_keys(lowered: str) -> list[str]:
    """`contents_artifact` -> contents_sha256; `failed_response_artifact` ->
    failed_response_sha256, response_sha256."""
    tokens = lowered.split("_")
    for end in range(len(tokens) - 1, 0, -1):
        if tokens[end] in PATH_WORDS:
            return [f"{'_'.join(tokens[start:end])}_sha256" for start in range(end)]
    return []


def number_variants(name: str) -> list[str]:
    """`artifacts` -> artifacts, artifact; `artifact` -> artifact, artifacts."""
    return [name, name[:-1]] if name.endswith("s") else [name, f"{name}s"]


def named_sha_keys(lowered: str) -> list[str]:
    """`<key>_sha256` and `<stem>_sha256`, each in singular and plural."""
    stems = [lowered, *(key[: -len("_sha256")] for key in stem_sha_keys(lowered))]
    return [f"{variant}_sha256" for stem in stems for variant in number_variants(stem)]


TYPE_SHA_KEYS = {
    "pdf": ("pdf_sha256", "local_pdf_sha256", "held_pdf_sha256"),
    "text": (
        "text_sha256",
        "txt_sha256",
        "extracted_text_sha256",
        "extraction_sha256",
        "layout_text_sha256",
    ),
    "image": ("image_sha256", "render_sha256", "renderer_sha256"),
}


def type_families(hint: str) -> list[str]:
    families: list[str] = []
    if "pdf" in hint:
        families.append("pdf")
    if "text" in hint or "txt" in hint or "extraction" in hint:
        families.append("text")
    if "image" in hint or "render" in hint:
        families.append("image")
    return families


def type_sha_keys(hint: str) -> list[str]:
    return [key for family in type_families(hint) for key in TYPE_SHA_KEYS[family]]


# Name parts of a pin key that say how it is hashed, or describe the hash or
# the file's own content, not which other file it pins.
HASH_WORDS = {
    "sha256",
    "sha256sum",
    "sum",
    "expected",
    "actual",
    "computed",
    "observed",
    "content",
    "body",
    "integrity",
    "fingerprint",
    "verification",
    "verified",
    "sha",
    "hash",
    "hashes",
    "checksum",
    "checksums",
    "digest",
    "digests",
    "hex",
    "hexdigest",
    "value",
    "recorded",
    "file",
    "sha2",
    "256",
}
# Pins of the record's own source file in every channel: compared with no
# file and matching none, they bar the record's own held files.
OWN_FILE_SHA_KEYS = ("source_sha256", "original_sha256")
# Qualifier words of pins that describe a derivative of the source (its text,
# a rendering, its metadata) or an auxiliary file, not the source file itself.
DERIVATIVE_PIN_WORDS = {
    "text",
    "txt",
    "extraction",
    "extracted",
    "layout",
    "raw",
    "selected",
    "utf8",
    "metadata",
    "render",
    "renderer",
    "image",
    "dependency",
    "dependencies",
    "contents",
    "response",
    "failed",
}


def is_pin_key(name: str) -> bool:
    """A normalised key name under which a sha256 pin may be recorded."""
    return any(
        word in name
        for word in ("sha", "hash", "checksum", "digest", "fingerprint", "integrity")
    )


def derivative_pin(name: str) -> bool:
    """True when every word of the pin's qualifier names a derivative
    (`raw_selected_utf8_sha256`, `layout_text_sha256`)."""
    qualifier = pin_qualifier(name)
    return bool(qualifier) and all(
        token in DERIVATIVE_PIN_WORDS for token in qualifier.split("_")
    )


def pin_qualifier(name: str) -> str:
    """What a pin key says it pins: `pdf_hash` -> pdf, `sha256_hex` -> ''."""
    return "_".join(token for token in name.split("_") if token and token not in HASH_WORDS)


def pin_key_family(name: str) -> str | None:
    """The file type a type-guessed pin key describes (`held_pdf_sha256` -> pdf)."""
    spelled = f"{pin_qualifier(name)}_sha256"
    for family, keys in TYPE_SHA_KEYS.items():
        if spelled in keys:
            return family
    return None


def value_type_hint(value: Any) -> str:
    if not isinstance(value, str):
        return ""
    suffix = Path(clean_path_string(value)).suffix.lower()
    if suffix == ".pdf":
        return "pdf"
    if suffix in {".txt", ".md"}:
        return "text"
    if suffix in IMAGE_EXTENSIONS:
        return "image"
    return ""


def file_strings(value: Any) -> list[str]:
    """The file names a path value names (see names_a_file), cleaned."""
    if isinstance(value, str):
        return [clean_path_string(value)] if names_a_file(value) else []
    if isinstance(value, list):
        return [name for item in value for name in file_strings(item)]
    if isinstance(value, dict):
        return [
            name
            for key, item in value.items()
            if key_is_pathish(key)
            for name in file_strings(item)
        ]
    return []


def only_file_of_families(key: str, context: dict[str, Any], families: set[str]) -> bool:
    """True when the one file under `key` is the only file of these types that
    `context` names, so a type-guessed pin can describe nothing else."""
    own = set(file_strings(context.get(key)))
    if len(own) != 1:
        return False
    others = {
        name
        for other_key, value in context.items()
        if key_is_pathish(other_key)
        for name in file_strings(value)
    } - own
    return not any(value_type_hint(name) in families for name in others)


def pins_for_path_key(key: str, context: dict[str, Any]) -> Pins:
    """The (hash key, pin) pairs recorded in `context` for the file under `key`.

    Candidate names are tried tier by tier and the first tier holding a pin
    wins.  Names for this key and plain pins are synonyms, so every one present
    must hold.  A type-guessed name may describe a sibling file of the same
    type, so only the first present is taken, unless the record names no other
    file of those types: then every one present must hold.
    """
    lowered = normal_key(key)
    takes_plain = lowered in GENERIC_SHA_PATH_KEYS or sole_file_valued_key(key, context)
    tiers = (
        (named_sha_keys(lowered), True),
        (type_sha_keys(lowered), False),
        (PLAIN_SHA_KEYS if takes_plain else (), True),
        (type_sha_keys(value_type_hint(context.get(key))), False),
        ((EACH_COPY_SHA_KEY,), True),
    )
    view = sha_view(context)
    for candidates, all_must_hold in tiers:
        pins = tuple(
            (candidate, pin)
            for candidate in dict.fromkeys(candidates)
            if (pin := recorded_pin(view.get(candidate))) is not None
        )
        if pins:
            if all_must_hold or only_file_of_families(
                key, context, {pin_key_family(hash_key) for hash_key, _pin in pins}
            ):
                return pins
            return pins[:1]
    return ()


def recorded_pins(record: dict[str, Any], *keys: str) -> Pins:
    """The pins recorded under exactly these keys."""
    view = sha_view(record)
    pins = ((key, recorded_pin(view.get(key))) for key in keys)
    return tuple((key, pin) for key, pin in pins if pin is not None)


def key_marks_other_role(key: str) -> bool:
    lowered = key.lower()
    return any(part in lowered for part in OTHER_ROLE_KEY_PARTS)


def key_names_own_file(key: str, context: dict[str, Any]) -> bool:
    """True when `key` names the record's own held file, which alone takes the
    record's identity: a generic path key, a source-file container, or the only
    pathish key that names a file.  Files under any other key (errata, reviews,
    derivatives, dependencies) are indexed with evidence only."""
    if key_marks_other_role(key):
        return False
    return (
        normal_key(key) in GENERIC_SHA_PATH_KEYS
        or normal_key(key) in SOURCE_FILE_CONTAINER_KEYS
        or sole_file_valued_key(key, context)
    )


class NamedFile(NamedTuple):
    path: str
    pins: Pins
    evidence: str
    other_role: bool
    inherited: bool  # the pins are the ones passed in, not the item's own


def named_files(
    value: Any, pins: Pins, evidence: str, other_role: bool = False
) -> list[NamedFile]:
    """Each file a path value names, with the pins it must match.

    This is the one definition of "the files a record names", used for pin
    checks and registration alike.  A dict item names the files under each of
    its pathish keys; an item's own pins for a key replace the inherited ones.
    """
    if isinstance(value, str):
        return [NamedFile(value, pins, evidence, other_role, True)]
    if isinstance(value, list):
        return [
            found
            for number, item in enumerate(value)
            for found in named_files(item, pins, f"{evidence}[{number}]", other_role)
        ]
    if not isinstance(value, dict):
        return []
    found: list[NamedFile] = []
    for key, item in value.items():
        if not (key_is_pathish(key) and names_a_file(item)):
            continue
        own = pins_for_path_key(key, value)
        role = other_role or not key_names_own_file(key, value)
        for named in named_files(item, own or pins, f"{evidence}.{key}", role):
            found.append(named._replace(inherited=named.inherited and not own))
    return found


def metadata_from_context(
    contexts: list[dict[str, Any]],
    *,
    include_generic_key: bool = False,
) -> RecordMeta:
    meta = RecordMeta()
    for context in contexts:
        meta.add_source_id(context.get("source_id"))
        meta.add_source_id(context.get("source_ids"))
        meta.add_source_id(context.get("source_key"))
        meta.add_bibkey(context.get("source_key"))
        meta.add_bibkey(context.get("bibliography_key"))
        meta.add_bibkey(context.get("bibliographic_key"))
        meta.add_bibkey(context.get("bibkey"))
        meta.add_bibkey(context.get("bibkeys"))
        if include_generic_key:
            meta.add_source_id(context.get("key"))
            meta.add_bibkey(context.get("key"))
        meta.add_title(context.get("title"))
        meta.add_title(context.get("chapter_title"))
        meta.add_title(context.get("source_title"))
        meta.add_version(context.get("version"))
        meta.add_version(context.get("version_label"))
        meta.add_version(context.get("edition"))
        meta.add_version(context.get("manifestation"))
        meta.add_body_state(context.get("body_state"))
        meta.add_access_basis(context.get("access_basis"))
        meta.add_access_basis(context.get("body_acquisition_standing"))
        meta.add_access_basis(context.get("access_statement"))
        meta.add_access_basis(context.get("acquisition_method"))
        meta.add_access_basis(context.get("acquisition_origin"))
        meta.add_access_basis(context.get("access_outcome"))
        meta.add_extent_verified(context.get("extent_verified"))
        meta.add_extent_verified(context.get("complete_extent_verified"))
        for block_key in ("bibliographic_identity", "identity"):
            block = context.get(block_key)
            if isinstance(block, dict):
                meta.add_source_id(block.get("source_key"))
                meta.add_bibkey(block.get("source_key"))
                meta.add_bibkey(block.get("key"))
                meta.add_title(block.get("title"))
        bm = context.get("bibliographic_metadata")
        if isinstance(bm, dict):
            meta.add_title(bm.get("title"))
            meta.add_version(bm.get("version_label"))
    return meta


def merged_meta(*metas: RecordMeta) -> RecordMeta:
    merged = RecordMeta()
    for meta in metas:
        merged.merge(meta)
    return merged


def add_evidence(meta: RecordMeta, evidence: str) -> RecordMeta:
    clone = RecordMeta()
    clone.merge(meta)
    clone.add_evidence(evidence)
    return clone


def note_pin_failure(
    index: HeldIndex,
    path: Path,
    evidence: str,
    detail: str,
    pin_mismatches: set[str],
) -> None:
    """Index `path` with the failure as evidence and bar it from this record's identity."""
    rel_path = index.relpath(path)
    if rel_path in pin_mismatches:
        return
    pin_mismatches.add(rel_path)
    mismatch_meta = RecordMeta()
    mismatch_meta.add_evidence(f"{evidence}: recorded sha256 mismatch ({detail})")
    record = index.add_file(path, mismatch_meta)
    index.stats.sha_mismatches.append(f"{evidence}: {record.path} {detail}")


def verify_pinned_path_value(
    index: HeldIndex,
    value: Any,
    root: Path,
    base_dir: Path | None,
    evidence: str,
    pins: Pins,
    allow_tmp: bool,
    pin_mismatches: set[str],
) -> bool:
    """Check every held file a path value names against its pins; True when
    some held file was compared with pins."""
    compared = False
    for named in named_files(value, pins, evidence):
        if not named.pins:
            continue
        path = resolve_named_path(named.path, root, base_dir)
        if path is None or not is_indexable_held_file(path, root, allow_tmp):
            continue
        compared = True
        if index.relpath(path) in pin_mismatches:
            continue
        detail = pin_failure(path, named.pins)
        if detail:
            note_pin_failure(index, path, named.evidence, detail, pin_mismatches)
    return compared


def note_uncompared_pins(index: HeldIndex, evidence: str, pins: Pins) -> None:
    """List pins whose record names no held file to compare them with."""
    for hash_key, pin in pins:
        shown = "is not a single sha256 hex digest" if pin == MALFORMED_PIN else pin
        note_unpaired(index, evidence, f"recorded {hash_key} {shown} names no held file to compare")


def register_path_value(
    index: HeldIndex,
    value: Any,
    root: Path,
    base_dir: Path | None,
    meta: RecordMeta,
    evidence: str,
    pins: Pins = (),
    allow_tmp: bool = False,
    pin_mismatches: set[str] | None = None,
) -> None:
    if pin_mismatches is None:
        pin_mismatches = set()
    for named in named_files(value, pins, evidence):
        path = resolve_named_path(named.path, root, base_dir)
        if path is None:
            missing = f"{named.evidence}: {named.path}"
            if (
                could_be_indexable_missing_path(named.path, root, base_dir, allow_tmp)
                and missing not in index.stats.missing_named_paths
            ):
                index.stats.missing_named_paths.append(missing)
            continue
        if not is_indexable_held_file(path, root, allow_tmp):
            continue
        if index.relpath(path) in pin_mismatches:
            continue
        if named.pins:
            detail = pin_failure(path, named.pins)
            if detail:
                note_pin_failure(index, path, named.evidence, detail, pin_mismatches)
                continue
        file_meta = RecordMeta() if named.other_role else meta
        index.add_file(path, add_evidence(file_meta, named.evidence))


def loose_pins(value: Any, label: str = "", under_pin_key: bool = False) -> list[tuple[str, str]]:
    """(label, pin) for every sha256 pin inside a record: a value under a
    hash-named key or inside a hash-named container, or an algorithm/value
    pair, at any depth.  A nested dict that names a file is a record of its own
    and is skipped.  A malformed value counts only under a sha256-named key.
    """
    found: list[tuple[str, str]] = []
    if isinstance(value, list):
        for number, item in enumerate(value):
            item_label = f"{label}[{number}]"
            if isinstance(item, str):
                pin = recorded_pin(item)
                if under_pin_key and pin not in (None, MALFORMED_PIN):
                    found.append((item_label, pin))
            else:
                found.extend(loose_pins(item, item_label, under_pin_key))
        return found
    if not isinstance(value, dict) or (label and names_file_record(value)):
        return found
    pair = recorded_pin(algorithm_pin(value))
    if pair is not None:
        found.append((label or "value", pair))
    has_algorithm = bool(algorithm_name(value))
    for key, item in value.items():
        name = normal_key(key)
        if has_algorithm and name in ALGORITHM_VALUE_KEYS:
            continue  # the pair above, or another algorithm's digest
        item_label = f"{label}.{key}" if label else str(key)
        inner = under_pin_key or is_pin_key(name)
        if isinstance(item, str):
            pin = recorded_pin(item)
            if inner and pin is not None and (pin != MALFORMED_PIN or "sha256" in name):
                found.append((item_label, pin))
        else:
            found.extend(loose_pins(item, item_label, inner))
    return found


def unmatched_pin_targets(
    name: str,
    held: list[Path],
    own_held: list[Path],
    plain_keys: tuple[str, ...],
    taken: set[str] | None = None,
    nested: bool = False,
) -> list[Path]:
    """The held files that a pin compared with no file, and matching none of
    them, describes and so bars.  `name` is the pin's normalised key.

    - A record-level pin bars every held file when it is a plain pin
      (`plain_keys`), a path key took it, or its name says only how it is
      hashed (`hash`, `sha256_hex`, `checksum`); a nested one does so only
      when the record names one held file.
    - An own-file pin (OWN_FILE_SHA_KEYS) bars the record's own held files.
    - A type-guessed pin (`pdf_sha256`) bars the held files of its type.
    - Any other pin bars the record's own file when the record names exactly
      one, unless every word of its qualifier names a derivative.
    An empty result leaves the pin unpaired.
    """
    hashed_only = not pin_qualifier(name)
    if nested:
        if len(held) == 1 and (hashed_only or name in plain_keys):
            return held
    elif hashed_only or name in plain_keys or name in (taken or set()):
        return held
    if name in OWN_FILE_SHA_KEYS:
        return own_held
    family = pin_key_family(name)
    typed = [path for path in held if family and value_type_hint(str(path)) == family]
    if typed and (not nested or len(held) == 1):
        return typed
    if len(own_held) == 1 and not derivative_pin(name):
        return own_held
    return []


def note_unpaired(index: HeldIndex, evidence: str, detail: str) -> None:
    item = f"{evidence}: {detail}"
    if item not in index.stats.unpaired_pins:
        index.stats.unpaired_pins.append(item)


def check_loose_pins(
    index: HeldIndex,
    obj: dict[str, Any],
    handled: set[str],
    actual: dict[Path, str],
    held: list[Path],
    own_held: list[Path],
    evidence: str,
    pin_mismatches: set[str],
    plain_keys: tuple[str, ...] = PLAIN_SHA_KEYS,
) -> None:
    """Every pin in the record not handled by the record-level rules must match
    a file the record names.  Otherwise it bars the files unmatched_pin_targets
    says it describes (`integrity.sha256`, `hashes[0]`, a sha256
    algorithm/value pair or a key of the file's type, when the record names
    one held file); any other unmatched pin is listed as unpaired."""
    for label, pin in loose_pins(obj):
        if pin in handled or pin in actual.values():
            continue
        shown = "is not a single sha256 hex digest" if pin == MALFORMED_PIN else pin
        detail = f"recorded {label} {shown} matches no file the record names"
        name = normal_key(re.sub(r"\[\d+\]", "", label).rsplit(".", 1)[-1])
        barred = unmatched_pin_targets(name, held, own_held, plain_keys, nested=True)
        for path in barred:
            note_pin_failure(
                index, path, evidence, f"{detail} (actual {actual[path]})", pin_mismatches
            )
        if not barred:
            note_unpaired(index, evidence, detail)


def subtree_held_files(
    obj: Any, root: Path, base_dir: Path | None, allow_tmp: bool
) -> tuple[list[Path], list[Path]]:
    """(held, own held) files that the records anywhere inside `obj` name."""
    held: dict[Path, bool] = {}

    def visit(value: Any) -> None:
        if isinstance(value, list):
            for item in value:
                visit(item)
        if not isinstance(value, dict):
            return
        for key, item in value.items():
            if key_is_pathish(key) and names_a_file(item):
                other_role = not key_names_own_file(key, value)
                for named in named_files(item, (), "", other_role):
                    path = resolve_named_path(named.path, root, base_dir)
                    if path is not None and is_indexable_held_file(path, root, allow_tmp):
                        held[path] = held.get(path, False) or not named.other_role
            visit(item)

    visit(obj)
    return list(held), [path for path, own in held.items() if own]


def check_record_pins(
    index: HeldIndex,
    root: Path,
    base_dir: Path | None,
    obj: dict[str, Any],
    evidence: str,
    pin_mismatches: set[str],
    allow_tmp: bool,
    plain_keys: tuple[str, ...] = PLAIN_SHA_KEYS,
    covered: bool = False,
) -> None:
    """Record-level pin rules for the files a record names.

    A malformed value under a sha256-named key withholds the record's identity
    from every held file the record names.  A pin (a sha, hash, checksum,
    digest, fingerprint or integrity key holding a sha256 digest) that was
    compared with no named file and matches none of them bars the files
    unmatched_pin_targets names, or else is listed as unpaired.  A pin keyed
    by a file name in a hash dict ({"a.pdf": digest}) must hold for that file.
    Pins nested deeper, in sub-dicts or lists that name no file, follow
    check_loose_pins.

    A record that names no existing file has its pins checked against the
    held files that the records nested inside it name (none, when it names a
    missing file itself), unless it is `covered`: a sub-dict naming no file,
    whose pins the enclosing record's check_loose_pins already reached.  A
    record naming only files of kinds the index does not hold (`notes.md`) is
    skipped: its pins describe those files.
    """
    named: dict[Path, None] = {}
    own: dict[Path, None] = {}
    taken: set[str] = set()
    compared: set[str] = set()
    for key, value in obj.items():
        if not (key_is_pathish(key) and names_a_file(value)):
            continue
        key_pins = pins_for_path_key(key, obj)
        taken.update(hash_key for hash_key, _pin in key_pins)
        other_role = not key_names_own_file(key, obj)
        for item in named_files(value, key_pins, evidence, other_role):
            path = resolve_named_path(item.path, root, base_dir)
            if path is None:
                continue
            named[path] = None
            if not item.other_role:
                own[path] = None
            if item.inherited:
                compared.update(hash_key for hash_key, _pin in item.pins)
    if not named:
        if covered and not names_file_record(obj):
            return
        if names_file_record(obj) and not any(
            key_is_pathish(key) and names_a_file(value) for key, value in obj.items()
        ):
            return  # its pins describe files of kinds the index does not hold (.md, .json)
        held: list[Path] = []
        own_held: list[Path] = []
        if not names_file_record(obj):
            held, own_held = subtree_held_files(obj, root, base_dir, allow_tmp)
        actual = {path: stream_sha256(path)[0] for path in held}
        check_loose_pins(
            index, obj, set(), actual, held, own_held, evidence, pin_mismatches, plain_keys
        )
        return
    held = [path for path in named if is_indexable_held_file(path, root, allow_tmp)]
    own_held = [path for path in held if path in own]
    view = sha_view(obj)
    malformed = sorted(
        key for key, value in view.items() if "sha256" in key and recorded_pin(value) == MALFORMED_PIN
    )
    if malformed:
        detail = f"recorded {malformed[0]} is not a single sha256 hex digest"
        for path in held:
            note_pin_failure(index, path, evidence, detail, pin_mismatches)
        return
    actual = {path: stream_sha256(path)[0] for path in named}
    for label, file_name, pin in file_keyed_pins(obj):
        target = resolve_named_path(file_name, root, base_dir)
        if target not in named:
            same_name = [path for path in named if path.name == Path(file_name).name]
            target = same_name[0] if len(same_name) == 1 else None
        if target is None:
            if pin not in actual.values():
                note_unpaired(
                    index, evidence, f"recorded {label} {pin} matches no file the record names"
                )
        elif target in held and actual[target] != pin:
            detail = f"recorded {label} {pin} actual {actual[target]}"
            note_pin_failure(index, target, evidence, detail, pin_mismatches)
    for key, value in view.items():
        pin = recorded_pin(value)
        if (
            not is_pin_key(key)
            or key in compared
            or pin is None
            or pin == MALFORMED_PIN
            or pin in actual.values()
        ):
            continue
        detail = f"recorded {key} {pin} matches no file the record names"
        barred = unmatched_pin_targets(key, held, own_held, plain_keys, taken)
        for path in barred:
            note_pin_failure(
                index, path, evidence, f"{detail} (actual {actual[path]})", pin_mismatches
            )
        if not barred:
            note_unpaired(index, evidence, detail)
    handled = {recorded_pin(value) for key, value in view.items() if is_pin_key(key)}
    handled.update(pin for _label, _name, pin in file_keyed_pins(obj))
    handled.discard(MALFORMED_PIN)
    check_loose_pins(
        index, obj, handled, actual, held, own_held, evidence, pin_mismatches, plain_keys
    )


def collect_filesystem(index: HeldIndex, directory: Path) -> None:
    if not directory.is_dir():
        return
    for path in sorted(directory.rglob("*")):
        if path.is_file() and path.suffix.lower() in WALK_EXTENSIONS:
            meta = RecordMeta()
            meta.add_evidence(f"filesystem walk:{index.relpath(path)}")
            index.add_file(path, meta)


def nested_pins(record: dict[str, Any], block_key: str) -> Pins:
    """The sha256 pin inside an identity block such as bibliographic_metadata."""
    block = record.get(block_key)
    if not isinstance(block, dict):
        return ()
    return tuple((f"{block_key}.{key}", pin) for key, pin in recorded_pins(block, "sha256"))


def bar_entry_files(
    index: HeldIndex,
    root: Path,
    values: list[tuple[Any, str, bool]],
    pin_mismatches: set[str],
) -> None:
    """Withhold an entry's identity from every held file it names, once any of
    its files failed a pin."""
    failed = ", ".join(sorted(pin_mismatches))
    for value, evidence, allow_tmp in values:
        for named in named_files(value, (), evidence):
            path = resolve_named_path(named.path, root, None)
            if path is not None and is_indexable_held_file(path, root, allow_tmp):
                detail = f"another file of this entry failed its recorded sha256 ({failed})"
                note_pin_failure(index, path, named.evidence, detail, pin_mismatches)


def collect_citations_manifest(index: HeldIndex, root: Path) -> None:
    manifest = root / "citations/manifest.json"
    if not manifest.is_file():
        return
    data = read_json(manifest)
    entries = data.get("entries", []) if isinstance(data, dict) else []
    for number, entry in enumerate(entries):
        if not isinstance(entry, dict):
            continue
        pin_mismatches: set[str] = set()
        contexts = [entry]
        bm = entry.get("bibliographic_metadata")
        if isinstance(bm, dict):
            contexts.append(bm)
        meta = metadata_from_context(contexts)
        meta.add_extent_verified(entry.get("extent_verified"))
        verification = entry.get("verification")
        if isinstance(verification, dict):
            meta.add_extent_verified(verification.get("extent_verified"))
        filename = entry.get("filename")
        copy_value = str(Path("citations") / filename) if isinstance(filename, str) else filename
        copy_evidence = f"citations/manifest.json:entries[{number}].filename"
        copy_pins = recorded_pins(entry, "sha256")
        originals = entry.get("original_paths", []) or []
        original_evidence = f"citations/manifest.json:entries[{number}].original_paths"
        # Pins named for original_paths (original_sha256, original_paths_sha256),
        # source_sha256 and the identity block's sha256 describe the originals.
        original_pins = tuple(
            dict.fromkeys(
                pins_for_path_key("original_paths", entry)
                + recorded_pins(entry, "source_sha256")
                + nested_pins(entry, "bibliographic_metadata")
            )
        )
        # Verify every pin first, so a failure bars every file of this entry.
        for value, evidence, pins, allow_tmp in (
            (copy_value, copy_evidence, copy_pins, False),
            (originals, original_evidence, original_pins, True),
        ):
            if not verify_pinned_path_value(
                index, value, root, None, evidence, pins, allow_tmp, pin_mismatches
            ):
                note_uncompared_pins(index, evidence, pins)
        held: dict[Path, str] = {}
        for value, allow_tmp in ((copy_value, False), (originals, True)):
            for named in named_files(value, (), ""):
                path = resolve_named_path(named.path, root, None)
                if path is not None and is_indexable_held_file(path, root, allow_tmp):
                    held[path] = stream_sha256(path)[0]
        handled = {pin for _key, pin in copy_pins + original_pins} - {MALFORMED_PIN}
        check_loose_pins(
            index,
            entry,
            handled,
            held,
            list(held),
            list(held),
            f"citations/manifest.json:entries[{number}]",
            pin_mismatches,
        )
        if pin_mismatches:
            bar_entry_files(
                index,
                root,
                [(copy_value, copy_evidence, False), (originals, original_evidence, True)],
                pin_mismatches,
            )
        register_path_value(
            index,
            copy_value,
            root,
            None,
            meta,
            copy_evidence,
            copy_pins,
            pin_mismatches=pin_mismatches,
        )
        register_path_value(
            index,
            originals,
            root,
            None,
            meta,
            original_evidence,
            original_pins,
            allow_tmp=True,
            pin_mismatches=pin_mismatches,
        )


def collect_filename_map(index: HeldIndex, root: Path) -> None:
    path = root / "citations/FILENAME-MAP.csv"
    if not path.is_file():
        return
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        for row_number, row in enumerate(reader, start=2):
            meta = RecordMeta()
            copied = row.get("copied_filename")
            if copied:
                register_path_value(
                    index,
                    str(Path("citations") / copied),
                    root,
                    None,
                    meta,
                    f"citations/FILENAME-MAP.csv:row {row_number} copied_filename",
                )
            original = row.get("original_path")
            pins = recorded_pins(row, "original_sha256")
            evidence = f"citations/FILENAME-MAP.csv:row {row_number} original_path"
            path = resolve_named_path(original, root, None)
            if path is None or not is_indexable_held_file(path, root, True):
                note_uncompared_pins(index, evidence, pins)
            if original:
                register_path_value(
                    index, original, root, None, meta, evidence, pins, allow_tmp=True
                )


def collect_json_pin_mismatches(
    index: HeldIndex,
    root: Path,
    base_dir: Path | None,
    obj: Any,
    expr: str,
    evidence_prefix: str,
    pin_mismatches: set[str],
    allow_tmp: bool,
    plain_keys: tuple[str, ...] = PLAIN_SHA_KEYS,
    covered: bool = False,
) -> None:
    """Check the pins of every record in a JSON value.  Every value inside a
    dict is `covered`: that dict's check reaches its pins (see
    check_record_pins)."""
    if isinstance(obj, dict):
        check_record_pins(
            index,
            root,
            base_dir,
            obj,
            f"{evidence_prefix}:{expr}" if expr else evidence_prefix,
            pin_mismatches,
            allow_tmp,
            plain_keys,
            covered,
        )
        for key, value in obj.items():
            if key_is_pathish(key):
                verify_pinned_path_value(
                    index,
                    value,
                    root,
                    base_dir,
                    f"{evidence_prefix}:{expr}.{key}" if expr else f"{evidence_prefix}:{key}",
                    pins_for_path_key(key, obj),
                    allow_tmp,
                    pin_mismatches,
                )
        children = list(obj.items())
    elif isinstance(obj, list):
        children = [(f"[{number}]", item) for number, item in enumerate(obj)]
    else:
        return
    for key, value in children:
        if isinstance(obj, dict):
            child_expr = f"{expr}.{key}" if expr else key
        else:
            child_expr = f"{expr}{key}"
        collect_json_pin_mismatches(
            index,
            root,
            base_dir,
            value,
            child_expr,
            evidence_prefix,
            pin_mismatches,
            allow_tmp,
            plain_keys,
            covered or isinstance(obj, dict),
        )


def walk_json_record(
    index: HeldIndex,
    root: Path,
    doc_path: Path,
    obj: Any,
    expr: str,
    inherited_identity: RecordMeta,
    pin_mismatches: set[str],
) -> None:
    """Register the files a JSON document names; its pins are already checked.

    tmp/ files are indexed (location_stable false), as for the queue.
    """
    evidence_prefix = index.relpath(doc_path)
    if isinstance(obj, dict):
        # A bare `key` field is an identity only at a record's top level, beside
        # an identity marker, or in a record that pins the file it names by
        # sha256; elsewhere (git trees, key/value lists) not.
        generic_key_is_identity = (
            re.fullmatch(r"(\[\d+\])?", expr) is not None
            or any(marker in obj for marker in IDENTITY_MARKER_KEYS)
            or any(
                pin != MALFORMED_PIN
                for key, value in obj.items()
                if key_is_pathish(key) and names_a_file(value)
                for _hash_key, pin in pins_for_path_key(key, obj)
            )
        )
        local_identity = metadata_from_context(
            [obj], include_generic_key=generic_key_is_identity
        )
        meta = merged_meta(inherited_identity, local_identity)
        for key, value in obj.items():
            key_expr = f"{expr}.{key}" if expr else key
            if key_is_pathish(key):
                register_path_value(
                    index,
                    value,
                    root,
                    doc_path.parent,
                    meta if key_names_own_file(key, obj) else RecordMeta(),
                    f"{evidence_prefix}:{key_expr}",
                    pins_for_path_key(key, obj),
                    allow_tmp=True,
                    pin_mismatches=pin_mismatches,
                )
            child_identity = RecordMeta()
            if key.lower() in SOURCE_FILE_CONTAINER_KEYS:
                child_identity.merge(meta)
            walk_json_record(
                index, root, doc_path, value, key_expr, child_identity, pin_mismatches
            )
    elif isinstance(obj, list):
        for number, item in enumerate(obj):
            walk_json_record(
                index,
                root,
                doc_path,
                item,
                f"{expr}[{number}]",
                inherited_identity,
                pin_mismatches,
            )
    elif isinstance(obj, str) and has_file_extension(obj):
        register_path_value(
            index,
            obj,
            root,
            doc_path.parent,
            inherited_identity,
            f"{evidence_prefix}:{expr}",
            allow_tmp=True,
            pin_mismatches=pin_mismatches,
        )


def collect_source_reference_json(index: HeldIndex, root: Path) -> None:
    directory = root / "source/references"
    if not directory.is_dir():
        return
    for path in sorted(directory.rglob("*.json")):
        try:
            data = read_json(path)
        except Exception as exc:
            index.stats.unreadable_json.append(f"{index.relpath(path)}: {exc}")
            continue
        # One set per document: a file failing any pin in it gets no identity from it.
        pin_mismatches: set[str] = set()
        collect_json_pin_mismatches(
            index, root, path.parent, data, "", index.relpath(path), pin_mismatches, True
        )
        walk_json_record(index, root, path, data, "", RecordMeta(), pin_mismatches)


README_EXT = r"\.(?:pdf|djvu|epub|html?|txt|png|jpe?g|tiff?|gif|webp|bmp|ps)(?![\w-]|\.\w)"
# A backticked or double-quoted name may contain spaces; a bare name may not.
README_TOKEN_RE = re.compile(
    rf"`([^`\n]+?{README_EXT})`"
    rf"|\"([^\"\n]+?{README_EXT})\""
    rf"|([^\s`\"'<>\[\]{{}}|*?,;]+{README_EXT})",
    re.IGNORECASE,
)


def readme_tokens(text: str) -> list[str]:
    return [next(group for group in match if group) for match in README_TOKEN_RE.findall(text)]


def readme_path_tokens(text: str, root: Path, base_dir: Path) -> list[str]:
    """Path tokens of a README; a whole line naming an existing file may hold spaces."""
    tokens: list[str] = []
    for line in text.splitlines():
        whole = line.strip().lstrip("-*+ \t")
        if (
            " " in whole
            and re.search(rf"{README_EXT}$", whole, re.IGNORECASE)
            and resolve_named_path(whole, root, base_dir) is not None
        ):
            tokens.append(whole)
        else:
            tokens.extend(readme_tokens(line))
    return tokens


def readme_names_file(text: str, name: str) -> bool:
    """True when `name` appears as a whole file name, not inside a longer one."""
    pattern = rf"(?<![\w./\\-]){re.escape(name)}(?![\w-]|\.\w)"
    return re.search(pattern, text) is not None


def collect_readme(index: HeldIndex, root: Path, path: Path) -> None:
    try:
        text = read_text(path)
    except UnicodeDecodeError as exc:
        index.stats.unreadable_json.append(f"{index.relpath(path)}: {exc}")
        return
    meta = RecordMeta()
    for token in readme_path_tokens(text, root, path.parent):
        register_path_value(
            index,
            token,
            root,
            path.parent,
            meta,
            f"{index.relpath(path)}:text reference",
        )
    for child in sorted(path.parent.iterdir()):
        if (
            child.is_file()
            and child.suffix.lower() in WALK_EXTENSIONS
            and readme_names_file(text, child.name)
        ):
            child_meta = RecordMeta()
            child_meta.add_evidence(f"{index.relpath(path)}:mentions {child.name}")
            index.add_file(child, child_meta)


def collect_readmes(index: HeldIndex, root: Path) -> None:
    directory = root / "source/references"
    if not directory.is_dir():
        return
    for path in sorted(directory.rglob("*")):
        if path.is_file() and path.name.upper().startswith(("README", "READING")):
            collect_readme(index, root, path)


def queue_path_fields(presentation: dict[str, Any]) -> Iterable[tuple[str, Any]]:
    for key in (
        "local_path",
        "local_artifact",
        "local_artifacts",
        "artifacts",
        "local_capture",
    ):
        if key in presentation:
            yield key, presentation[key]


# Presentation-level pins, with bibliographic_identity.sha256: each must hold
# for every file the presentation lists.
QUEUE_SHA_KEYS = ("sha256", "recorded_sha256", "source_sha256")


def collect_queue(index: HeldIndex, root: Path) -> None:
    if not QUEUE.is_file() and root == ROOT:
        return
    queue = root / "spec/coverage/edition-2026/completion-work-queue.jsonl"
    if not queue.is_file():
        return
    with queue.open("r", encoding="utf-8-sig") as handle:
        for line_number, line in enumerate(handle, start=1):
            line = line.strip()
            if not line:
                continue
            try:
                row = json.loads(line)
            except json.JSONDecodeError as exc:
                index.stats.unreadable_json.append(
                    f"spec/coverage/edition-2026/completion-work-queue.jsonl:line {line_number}: {exc}"
                )
                continue
            if not isinstance(row, dict):
                continue
            presentations = row.get("source_presentations") or []
            if not isinstance(presentations, list):
                continue
            for presentation_number, presentation in enumerate(presentations):
                if not isinstance(presentation, dict):
                    continue
                pin_mismatches: set[str] = set()
                meta = metadata_from_context([presentation])
                meta.add_body_state(row.get("body_state"))
                meta.add_access_basis(row.get("body_acquisition_standing"))
                identity_pins = nested_pins(presentation, "bibliographic_identity")
                pins = recorded_pins(presentation, *QUEUE_SHA_KEYS) + identity_pins
                prefix = (
                    "spec/coverage/edition-2026/completion-work-queue.jsonl:"
                    f"line {line_number} source_presentations[{presentation_number}]"
                )
                for key, value in queue_path_fields(presentation):
                    verify_pinned_path_value(
                        index, value, root, None, f"{prefix}.{key}", pins, True, pin_mismatches
                    )
                # The identity block's pin is a presentation pin: it must also
                # match some listed file when every listed file has its own pin.
                collect_json_pin_mismatches(
                    index,
                    root,
                    None,
                    {**presentation, **dict(identity_pins)},
                    "",
                    prefix,
                    pin_mismatches,
                    True,
                    (*PLAIN_SHA_KEYS, *QUEUE_SHA_KEYS, *(key for key, _pin in identity_pins)),
                )
                for key, value in queue_path_fields(presentation):
                    register_path_value(
                        index,
                        value,
                        root,
                        None,
                        meta,
                        f"{prefix}.{key}",
                        pins,
                        True,
                        pin_mismatches,
                    )


def collect_frozen_source(index: HeldIndex, root: Path) -> None:
    """The frozen Version 1.0 manuscript (FLRV1) whose FLRV1-U* units the queue presents."""
    for name in ("formal-logic-reference.tex", "formal-logic-reference.pdf"):
        path = root / "source" / name
        if path.is_file():
            meta = RecordMeta()
            meta.add_source_id("FLRV1")
            meta.add_title("Formal Logic Reference")
            meta.add_version("Version 1.0 (frozen source manuscript)")
            meta.add_evidence(f"frozen source:{index.relpath(path)}")
            index.add_file(path, meta)


def build_index(root: Path = ROOT) -> tuple[dict[str, Any], BuildStats]:
    root = root.resolve()
    index = HeldIndex(root)
    collect_frozen_source(index, root)
    collect_filesystem(index, root / "citations")
    collect_filesystem(index, root / "source/references")
    collect_citations_manifest(index, root)
    collect_filename_map(index, root)
    collect_source_reference_json(index, root)
    collect_readmes(index, root)
    collect_queue(index, root)
    return index_to_output(index), index.stats


def write_json_atomic(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    fd, tmp_name = tempfile.mkstemp(
        prefix=f".{path.name}.", suffix=".tmp", dir=str(path.parent)
    )
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(payload)
        os.replace(tmp_name, path)
    except Exception:
        try:
            os.unlink(tmp_name)
        except OSError:
            pass
        raise


def is_held_sources_json(path: Path) -> bool:
    try:
        data = read_json(path)
    except Exception:
        return False
    return (
        isinstance(data, dict)
        and isinstance(data.get("entries"), list)
        and isinstance(data.get("source_index"), dict)
    )


def validate_out_path(out: Path, root: Path) -> str | None:
    resolved = out.resolve()
    forbidden_roots = [
        root / "citations",
        root / "source",
        root / "handbook/restoration",
        root / "handbook/generated",
    ]
    for forbidden in forbidden_roots:
        if is_under(resolved, forbidden):
            return f"refusing --out inside protected tree: {resolved}"

    allowed_roots = [root / "spec/coverage", root / "tmp"]
    if not any(is_under(resolved, allowed) for allowed in allowed_roots):
        return f"refusing --out outside spec/coverage/ or tmp/: {resolved}"

    if resolved.exists() and not is_held_sources_json(resolved):
        return f"refusing to overwrite non-held-sources JSON: {resolved}"
    return None


def summary_lines(data: dict[str, Any], stats: BuildStats, out: Path, apply: bool) -> list[str]:
    entries = data["entries"]
    pdf_entries = [entry for entry in entries if entry["kind"] == "pdf"]
    page_counted = sum(entry["pdf_pages"] is not None for entry in pdf_entries)
    evidence_count = sum(len(entry["evidence"]) for entry in entries)
    action = "wrote" if apply else "dry run"
    lines = [
        f"held_sources build {action}",
        f"out: {out}",
        f"entries: {len(entries)}",
        f"source_ids: {len(data['source_index'])}",
        f"pdfs: {len(pdf_entries)} ({page_counted} page counts, {len(pdf_entries) - page_counted} unknown)",
        f"evidence_links: {evidence_count}",
        f"missing_named_paths: {len(stats.missing_named_paths)}",
        f"recorded_sha_mismatches: {len(stats.sha_mismatches)}",
        f"unpaired_pins: {len(stats.unpaired_pins)}",
        f"unreadable_records: {len(stats.unreadable_json)}",
        *(
            f"{name}_conflicts: {len(stats.value_conflicts.get(name, []))}"
            for name in ("version", "body_state", "access_basis", "extent_verified")
        ),
    ]
    if stats.unreadable_json:
        lines.append("unreadable_record_details (JSON, queue lines, README text):")
        lines.extend(f"  - {item}" for item in stats.unreadable_json)
    if stats.value_conflicts:
        lines.append("recorded_value_conflict_details (output null):")
        for name, items in stats.value_conflicts.items():
            lines.extend(f"  - {name} {item}" for item in items)
    if stats.sha_mismatches:
        lines.append("recorded_sha_mismatch_details:")
        for mismatch in stats.sha_mismatches:
            lines.append(f"  - {mismatch}")
    if stats.unpaired_pins:
        lines.append("unpaired_pin_details (compared with no file; identity kept; exit 1 under --strict):")
        for unpaired in stats.unpaired_pins:
            lines.append(f"  - {unpaired}")
    if not apply:
        lines.append("no files written; pass --apply to write")
    return lines


def normalize_lookup_path(query: str, root: Path) -> str:
    path = resolve_named_path(query, root, None)
    if path is not None:
        try:
            return path.resolve().relative_to(root.resolve()).as_posix()
        except ValueError:
            return path.resolve().as_posix()
    return clean_path_string(query)


def lookup(data: dict[str, Any], query: str, root: Path = ROOT) -> list[dict[str, Any]]:
    if query in data["source_index"]:
        paths = set(data["source_index"][query])
        return [entry for entry in data["entries"] if entry["path"] in paths]
    normalized = normalize_lookup_path(query, root)
    normalized_alt = normalized.replace("\\", "/")
    return [
        entry
        for entry in data["entries"]
        if entry["path"] == normalized_alt or entry["path"].endswith("/" + normalized_alt)
    ]


def run_build(args: argparse.Namespace) -> int:
    out = Path(args.out) if args.out else DEFAULT_OUT
    if not out.is_absolute():
        out = ROOT / out
    out = out.resolve()
    refusal = validate_out_path(out, ROOT)
    if refusal:
        print(refusal, file=sys.stderr)
        return 1
    data, stats = build_index(ROOT)
    if args.apply:
        write_json_atomic(out, data)
    print("\n".join(summary_lines(data, stats, out, args.apply)))
    return build_exit_code(stats, args.strict)


def build_exit_code(stats: BuildStats, strict: bool) -> int:
    """1 for recorded sha256 mismatches, and under --strict for unpaired pins."""
    return 1 if stats.sha_mismatches or (strict and stats.unpaired_pins) else 0


def run_lookup(args: argparse.Namespace) -> int:
    if DEFAULT_OUT.is_file():
        data = read_json(DEFAULT_OUT)
    else:
        data, _stats = build_index(ROOT)
    matches = lookup(data, args.query, ROOT)
    if not matches:
        print(f"no held source match for {args.query}", file=sys.stderr)
        return 1
    print(json.dumps(matches, ensure_ascii=False, indent=2, sort_keys=True))
    return 0


def selftest_pdf(path: Path) -> None:
    try:
        from pypdf import PdfWriter  # type: ignore

        writer = PdfWriter()
        writer.add_blank_page(width=72, height=72)
        with path.open("wb") as handle:
            writer.write(handle)
    except Exception:
        path.write_bytes(
            b"%PDF-1.4\n1 0 obj<<>>endobj\n"
            b"trailer<<>>\n%%EOF\n"
        )


def run_selftest() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        (root / "citations").mkdir()
        refs = root / "source/references/demo"
        refs.mkdir(parents=True)
        adv_refs = root / "source/references/adv"
        adv_refs.mkdir(parents=True)
        adv3_refs = root / "source/references/adv3"
        adv3_refs.mkdir(parents=True)
        adv4_refs = root / "source/references/adv4"
        adv4_refs.mkdir(parents=True)
        queue_dir = root / "spec/coverage/edition-2026"
        queue_dir.mkdir(parents=True)
        tmp_dir = root / "tmp"
        tmp_dir.mkdir()

        pdf = root / "citations/demo.pdf"
        selftest_pdf(pdf)
        pdf_sha, pdf_bytes = stream_sha256(pdf)

        mismatched_pdf = root / "citations/a.pdf"
        selftest_pdf(mismatched_pdf)
        bad_sha = "0" * 64

        citation_order_pdf = root / "citations/c.pdf"
        selftest_pdf(citation_order_pdf)

        text = refs / "demo.txt"
        text.write_text("demo source\n", encoding="utf-8", newline="\n")
        text_sha, text_bytes = stream_sha256(text)

        other_pdf = refs / "other.pdf"
        selftest_pdf(other_pdf)

        adv_pdf = adv_refs / "a.pdf"
        selftest_pdf(adv_pdf)

        adv3_pdf = adv3_refs / "a.pdf"
        selftest_pdf(adv3_pdf)

        adv4_pdf = adv4_refs / "b.pdf"
        selftest_pdf(adv4_pdf)

        z1 = refs / "z1/resp.html"
        z2 = refs / "z2/resp.html"
        z1.parent.mkdir()
        z2.parent.mkdir()
        html_bytes = b"<html><title>challenge</title></html>\n"
        z1.write_bytes(html_bytes)
        z2.write_bytes(html_bytes)
        html_sha, _html_bytes_count = stream_sha256(z1)

        queue_pdf = tmp_dir / "q.pdf"
        selftest_pdf(queue_pdf)
        queue_pdf_sha, _queue_pdf_bytes = stream_sha256(queue_pdf)

        bad_queue_pdf = tmp_dir / "b.pdf"
        selftest_pdf(bad_queue_pdf)

        artifact_only_bad_pdf = tmp_dir / "c.pdf"
        selftest_pdf(artifact_only_bad_pdf)

        queue_order_bad_pdf = tmp_dir / "d.pdf"
        selftest_pdf(queue_order_bad_pdf)

        image = refs / "figure.png"
        image.write_bytes(b"\x89PNG\r\n\x1a\n")

        (root / "citations/manifest.json").write_text(
            json.dumps(
                {
                    "entries": [
                        {
                            "filename": "demo.pdf",
                            "sha256": pdf_sha,
                            "bytes": pdf_bytes,
                            "bibliographic_metadata": {
                                "title": "Demo Paper",
                                "version_label": "author copy",
                            },
                        },
                        {
                            "filename": "a.pdf",
                            "sha256": bad_sha,
                            "source_id": "SRC-A",
                            "version": "v9",
                            "extent_verified": True,
                        },
                        {
                            "filename": "c.pdf",
                            "original_paths": ["citations/c.pdf"],
                            "source_sha256": bad_sha,
                            "source_id": "C4",
                            "version": "v4",
                        },
                    ]
                }
            )
            + "\n",
            encoding="utf-8",
            newline="\n",
        )
        (root / "citations/FILENAME-MAP.csv").write_text(
            "original_path,copied_filename,original_sha256,source_page_range_zero_based\n"
            f"source/references/demo/demo.txt,demo.pdf,{text_sha},[]\n",
            encoding="utf-8",
            newline="\n",
        )
        (refs / "manifest.json").write_text(
            json.dumps(
                {
                    "source_key": "DemoKey",
                    "title": "Demo Text",
                    "manifestation": "Demo manifestation",
                    "source_files": [
                        {
                            "path": "demo.txt",
                            "bytes": text_bytes,
                            "sha256": text_sha,
                            "standing": "held text",
                            "extent_verified": True,
                        }
                    ],
                }
            )
            + "\n",
            encoding="utf-8",
            newline="\n",
        )
        (refs / "nested.json").write_text(
            json.dumps(
                {
                    "source_key": "KeyY",
                    "manifestation": "Y-ed2",
                    "related": {"dependency_pdf": "other.pdf"},
                }
            )
            + "\n",
            encoding="utf-8",
            newline="\n",
        )
        (refs / "hash-demo.json").write_text(
            json.dumps(
                {
                    "source_key": "KeyZ1",
                    "local_capture": "z1/resp.html",
                    "sha256": html_sha,
                }
            )
            + "\n",
            encoding="utf-8",
            newline="\n",
        )
        (adv_refs / "r1.json").write_text(
            json.dumps(
                {
                    "source_key": "K1",
                    "version": "v9",
                    "local_pdf": "a.pdf",
                    "sha256": bad_sha,
                    "source_files": ["a.pdf"],
                }
            )
            + "\n",
            encoding="utf-8",
            newline="\n",
        )
        (adv3_refs / "order.json").write_text(
            json.dumps(
                {
                    "source_key": "K1",
                    "version": "v1",
                    "source_files": [
                        {"path": "a.pdf"},
                        {"path": "a.pdf", "sha256": bad_sha},
                    ],
                }
            )
            + "\n",
            encoding="utf-8",
            newline="\n",
        )
        (adv4_refs / "child.json").write_text(
            json.dumps(
                {
                    "source_key": "K2",
                    "version": "v2",
                    "source_files": ["b.pdf"],
                    "x": {"pdf": "b.pdf", "pdf_sha256": bad_sha},
                }
            )
            + "\n",
            encoding="utf-8",
            newline="\n",
        )
        (refs / "README.md").write_text(
            "The figure is `figure.png`.\n",
            encoding="utf-8",
            newline="\n",
        )
        queue_row = {
            "title": "Work Unit Title",
            "body_state": "held",
            "body_acquisition_standing": "row-level standing",
            "source_presentations": [
                {
                    "source_id": "SRC-TEST",
                    "bibliographic_identity": {"key": "DemoBib"},
                    "title": "Demo Presentation",
                    "version": "v1",
                    "local_artifact": "citations/demo.pdf",
                    "sha256": pdf_sha,
                    "body_state": "held",
                    "body_acquisition_standing": "local test capture",
                },
                {
                    "source_id": "SRC-Q",
                    "bibliographic_identity": {"key": "BibQ"},
                    "title": "Queue Dict Artifact",
                    "version": "queue-v1",
                    "artifacts": [
                        {
                            "path": "tmp/q.pdf",
                            "recorded_sha256": queue_pdf_sha,
                        }
                    ],
                },
                {
                    "source_id": "Q1",
                    "title": "Queue Pin Bypass",
                    "version": "blocked-queue",
                    "sha256": bad_sha,
                    "local_artifact": "tmp/b.pdf",
                    "artifacts": [{"path": "tmp/b.pdf"}],
                },
                {
                    "source_id": "Q2",
                    "title": "Queue Enclosing Sha",
                    "version": "blocked-artifact",
                    "sha256": bad_sha,
                    "artifacts": [{"path": "tmp/c.pdf"}],
                },
                {
                    "source_id": "Q3",
                    "title": "Queue Artifact Order",
                    "version": "v3",
                    "local_artifact": "tmp/d.pdf",
                    "artifacts": [{"path": "tmp/d.pdf", "sha256": bad_sha}],
                },
            ],
        }
        (queue_dir / "completion-work-queue.jsonl").write_text(
            json.dumps(queue_row) + "\n", encoding="utf-8", newline="\n"
        )

        # Round-4 fixtures: generic sha pins on other local-file keys, list
        # records in one document, README token boundaries, missing-path
        # de-duplication and tmp originals named by the citations manifest.
        adv5_refs = root / "source/references/adv5"
        adv5_refs.mkdir(parents=True)
        for name in ("a.pdf", "b.pdf", "c.pdf", "data.pdf", "f.pdf"):
            selftest_pdf(adv5_refs / name)
        (adv5_refs / "e.html").write_bytes(html_bytes)
        adv5_records = {
            "A.json": {
                "source_key": "KA",
                "version": "vA",
                "local_capture": "a.pdf",
                "sha256": bad_sha,
            },
            "B.json": {
                "source_key": "KB",
                "version": "vB",
                "pdf_path": "b.pdf",
                "sha256": bad_sha,
            },
            "C.json": [
                {"source_key": "KC", "version": "vC", "path": "c.pdf", "sha256": bad_sha},
                {"source_key": "KC", "version": "vC", "path": "c.pdf"},
            ],
            "E.json": {
                "source_key": "KE",
                "captures": [{"local_capture": "e.html", "sha256": bad_sha}],
            },
            "F.json": {
                "source_key": "KF",
                "scan_image": "f.pdf",
                "sha256": bad_sha,
            },
            "M.json": {"source_key": "KM", "local_path": "gone.pdf"},
        }
        for name, record in adv5_records.items():
            (adv5_refs / name).write_text(
                json.dumps(record) + "\n", encoding="utf-8", newline="\n"
            )
        (adv5_refs / "README.md").write_text(
            "See data.pdf here. Also `spaced name.pdf`.\n- bare spaced (1).pdf\n",
            encoding="utf-8",
            newline="\n",
        )
        selftest_pdf(adv5_refs / "spaced name.pdf")
        selftest_pdf(adv5_refs / "bare spaced (1).pdf")
        orig_pdf = tmp_dir / "orig.pdf"
        selftest_pdf(orig_pdf)
        orig_sha, _orig_bytes = stream_sha256(orig_pdf)
        bad_orig_pdf = tmp_dir / "bad-orig.pdf"
        selftest_pdf(bad_orig_pdf)
        manifest_path = root / "citations/manifest.json"
        manifest_data = read_json(manifest_path)
        manifest_data["entries"].extend(
            [
                {
                    "filename": "demo.pdf",
                    "original_paths": ["tmp/orig.pdf"],
                    "source_sha256": orig_sha,
                    "source_id": "ORIG",
                },
                {
                    "filename": "demo.pdf",
                    "original_paths": ["tmp/bad-orig.pdf"],
                    "source_sha256": bad_sha,
                    "source_id": "BADORIG",
                },
            ]
        )
        manifest_path.write_text(
            json.dumps(manifest_data) + "\n", encoding="utf-8", newline="\n"
        )

        # Round-6 fixtures: hashes paired by stem, plain hashes that no path key
        # takes, malformed or prefixed pins, item-level type hashes, queue
        # presentation pins, nested generic `key` fields and other-role keys.
        r6 = root / "source/references/r6"
        r6_records: dict[str, Any] = {
            "F1": {"source_key": "R6F1", "version": "v", "contents_artifact": "a.pdf", "contents_sha256": bad_sha},
            "F2": {"source_key": "R6F2", "version": "v", "source_path": "a.pdf", "source_sha256": bad_sha},
            "F2b": {"source_key": "R6F2b", "version": "v", "dependency_pdf": "a.pdf", "dependency_sha256": bad_sha},
            "F2c": {"source_key": "R6F2c", "version": "v", "derived_file": "b.txt", "derived_sha256": bad_sha},
            "F3": {"source_key": "R6F3", "version": "v", "scan_image": "a.pdf", "text_path": "b.txt", "sha256": bad_sha},
            "F4": {"source_key": "R6F4", "version": "v", "local_pdf": "a.pdf", "hashes": {"sha256": bad_sha}},
            "F5b": {
                "source_key": "R6F5b",
                "version": "v",
                "author_archive_local_file": "a.pdf",
                "repository_local_file": "b.txt",
                "sha256_each_copy": bad_sha,
            },
            "F10": {"source_key": "R6F10", "version": "v", "local_pdf": "a.pdf", "sha256": "sha256:" + bad_sha},
            "F10m": {"source_key": "R6F10m", "version": "v", "local_pdf": "a.pdf", "sha256": "f 4 e 35 not hex"},
            "F11": {"source_key": "R6F11", "version": "v", "source_files": [{"path": "a.pdf", "pdf_sha256": bad_sha}]},
        }
        r6_fail_files = {
            "F1": ["a.pdf"],
            "F2": ["a.pdf"],
            "F2b": ["a.pdf"],
            "F2c": ["b.txt"],
            "F3": ["a.pdf", "b.txt"],
            "F4": ["a.pdf"],
            "F5b": ["a.pdf", "b.txt"],
            "F10": ["a.pdf"],
            "F10m": ["a.pdf"],
            "F11": ["a.pdf"],
        }
        for name in [*r6_records, "ok", "okdep", "ok3", "F13", "okkey"]:
            (r6 / name).mkdir(parents=True)
            selftest_pdf(r6 / name / "a.pdf")
            (r6 / name / "b.txt").write_text(f"{name}\n", encoding="utf-8", newline="\n")
        ok_pdf_sha, _ok_bytes = stream_sha256(r6 / "ok/a.pdf")
        ok_txt_sha, _ok_txt_bytes = stream_sha256(r6 / "ok/b.txt")
        ok3_txt_sha, _ok3_bytes = stream_sha256(r6 / "ok3/b.txt")
        okdep_sha, _okdep_bytes = stream_sha256(r6 / "okdep/a.pdf")
        okkey_sha, _okkey_bytes = stream_sha256(r6 / "okkey/a.pdf")
        r6_records["ok"] = {
            "source_key": "R6OK",
            "version": "v-ok",
            "derived_file": "b.txt",
            "derived_sha256": ok_txt_sha,
            "local_pdf": "a.pdf",
            "sha256": "SHA256:" + ok_pdf_sha.upper(),
        }
        r6_records["okdep"] = {
            "source_key": "R6DEP",
            "version": "v-dep",
            "dependency_pdf": "a.pdf",
            "dependency_sha256": okdep_sha,
        }
        r6_records["ok3"] = {
            "source_key": "R6OK3",
            "scan_image": "a.pdf",
            "text_path": "b.txt",
            "sha256": ok3_txt_sha,
        }
        r6_records["F13"] = {"tree": [{"key": "pdf-blob", "path": "a.pdf"}]}
        r6_records["okkey"] = {
            "notes": {"key": "R6KEY", "file": "a.pdf", "sha256": okkey_sha}
        }
        for name, record in r6_records.items():
            (r6 / name / "r.json").write_text(
                json.dumps(record) + "\n", encoding="utf-8", newline="\n"
            )
        for name in ("q6.pdf", "q7.pdf"):
            selftest_pdf(tmp_dir / name)
        with (queue_dir / "completion-work-queue.jsonl").open(
            "a", encoding="utf-8", newline="\n"
        ) as handle:
            handle.write(
                json.dumps(
                    {
                        "source_presentations": [
                            {
                                "source_id": "R6Q6",
                                "version": "v",
                                "artifacts": [{"path": "tmp/q6.pdf", "pdf_sha256": bad_sha}],
                            },
                            {
                                "source_id": "R6Q7",
                                "version": "v",
                                "local_path": "tmp/q7.pdf",
                                "source_sha256": bad_sha,
                            },
                        ]
                    }
                )
                + "\n"
            )

        # Round-7 fixtures: content-decided kind, item files named by any
        # pathish key, plain pins every item overrides, further pin spellings,
        # unpaired pins, conflicting pins and tmp files named by source JSON.
        r7 = root / "source/references/r7"
        r7.mkdir(parents=True)
        (r7 / "challenge.pdf").write_bytes(b"<!DOCTYPE html>\n<html><body>challenge</body></html>\n")
        (r7 / "junk.pdf").write_bytes(b"not a pdf at all\n")
        junk_prefixed = r7 / "prefixed.pdf"
        selftest_pdf(junk_prefixed)
        junk_prefixed.write_bytes(b"\r\n \x00\xff\x1b\n" + junk_prefixed.read_bytes())
        r7_fail = {
            "t1a": {"source_files": [{"filename": "a.pdf"}], "sha256": bad_sha},
            "t1b": {"source_files": [{"file": "a.pdf"}], "sha256": bad_sha},
            "t1c": {"source_files": [{"pdf": "a.pdf"}], "sha256": bad_sha},
            "t1d": {"source_files": [{"local_capture": "a.pdf"}], "recorded_sha256": bad_sha},
            "t3": {"artifacts": ["a.pdf"], "artifact_sha256": bad_sha},
            "t4": {"local_pdf": "a.pdf", "file_sha256": bad_sha},
            "t5": {"local_pdf": "a.pdf", "checksums": {"sha256": bad_sha}},
            "t6": {"local_pdf": "a.pdf", "sha-256": bad_sha},
        }
        r7_override = {
            "t2b": ("artifacts", "artifact_sha256"),
            "t2c": ("source_files", "recorded_sha256"),
        }
        for name in [*r7_fail, *r7_override, "t2", "t7", "t8", "ok1", "unpaired"]:
            (r7 / name).mkdir()
            selftest_pdf(r7 / name / "a.pdf")
        t2_sha = stream_sha256(r7 / "t2/a.pdf")[0]
        r7_fail["t2"] = {
            "sha256": bad_sha,
            "source_files": [{"path": "a.pdf", "sha256": t2_sha}],
        }
        for name, (path_key, hash_key) in r7_override.items():
            own_sha = stream_sha256(r7 / name / "a.pdf")[0]
            r7_fail[name] = {hash_key: bad_sha, path_key: [{"path": "a.pdf", "sha256": own_sha}]}
        r7_fail["t7"] = {
            "local_pdf": "a.pdf",
            "sha256": stream_sha256(r7 / "t7/a.pdf")[0],
            "hashes": {"sha256": bad_sha},
        }
        r7_fail["t8"] = {
            "source_files": [{"path": "missing.pdf"}, {"path": "a.pdf", "sha256": stream_sha256(r7 / "t8/a.pdf")[0]}],
            "sha256": bad_sha,
        }
        r7_records: dict[str, Any] = {
            name: {"source_key": f"R7{name}", "version": "v", **record}
            for name, record in r7_fail.items()
        }
        r7_records["ok1"] = {
            "source_key": "R7ok1",
            "version": "v",
            "source_files": [{"filename": "a.pdf", "sha256": stream_sha256(r7 / "ok1/a.pdf")[0]}],
        }
        r7_records["unpaired"] = {
            "source_key": "R7unpaired",
            "local_pdf": "a.pdf",
            "pdf_sha256": stream_sha256(r7 / "unpaired/a.pdf")[0],
            "extraction_sha256": bad_sha,
        }
        for name, record in r7_records.items():
            (r7 / name / "r.json").write_text(
                json.dumps(record) + "\n", encoding="utf-8", newline="\n"
            )
        selftest_pdf(tmp_dir / "r7-preview.pdf")
        selftest_pdf(tmp_dir / "r7-t2.pdf")
        (r7 / "tmpbad.json").write_text(
            json.dumps(
                {
                    "source_key": "R7tmpbad",
                    "sha256": bad_sha,
                    "source_files": [
                        {"path": "tmp/r7-t2.pdf", "sha256": stream_sha256(tmp_dir / "r7-t2.pdf")[0]}
                    ],
                }
            )
            + "\n",
            encoding="utf-8",
            newline="\n",
        )
        (r7 / "tmpref.json").write_text(
            json.dumps({"source_key": "R7tmp", "local_path": "tmp/r7-preview.pdf"}) + "\n",
            encoding="utf-8",
            newline="\n",
        )

        # Round-8 fixtures: type-guessed pins contradicting the record's only
        # file of that type, further pin spellings, identity-block pins, own
        # files versus other files, and text that mentions %PDF-.
        r8 = root / "source/references/r8"
        r8_fail = {
            "S10": {"pdf_sha256": bad_sha, "source_files": [{"path": "a.pdf"}]},
            "S1": {"source_pdf": "a.pdf", "pdf_sha256": "GOOD", "held_pdf_sha256": bad_sha},
            "S2hex": {"local_pdf": "a.pdf", "sha256_hex": bad_sha},
            "S2hash": {"local_pdf": "a.pdf", "hash": bad_sha},
            "S2checksum": {"local_pdf": "a.pdf", "checksum": "sha256:" + bad_sha},
            "S2files": {"local_pdf": "a.pdf", "file_hashes": {"a.pdf": bad_sha}},
            "S2nested": {"local_pdf": "a.pdf", "hashes": {"a.pdf": {"sha256": bad_sha}}},
            "S3text": {"local_pdf": "a.pdf", "text_file": "b.txt", "txt_sha256": bad_sha},
        }
        r8_keep = {
            "S2filesok": {"local_pdf": "a.pdf", "file_hashes": {"a.pdf": "GOOD"}},
            "S2layout": {"local_pdf": "a.pdf", "sha256": "GOOD", "layout_sha256": bad_sha},
            "S2pdfhash": {"local_pdf": "a.pdf", "pdf_hash": "GOOD"},
        }
        for name in [*r8_fail, *r8_keep, "S6"]:
            (r8 / name).mkdir(parents=True)
            selftest_pdf(r8 / name / "a.pdf")
            (r8 / name / "b.txt").write_text(f"{name}\n", encoding="utf-8", newline="\n")
        selftest_pdf(r8 / "S6/b.pdf")
        selftest_pdf(r8 / "S6/c.pdf")
        for name, record in [*r8_fail.items(), *r8_keep.items()]:
            good = stream_sha256(r8 / name / "a.pdf")[0]
            text = json.dumps({"source_key": name, "version": f"v-{name}", **record})
            (r8 / name / "r.json").write_text(
                text.replace("GOOD", good) + "\n", encoding="utf-8", newline="\n"
            )
        (r8 / "S6/r.json").write_text(
            json.dumps(
                {
                    "source_key": "S6",
                    "version": "v6",
                    "local_pdf": "a.pdf",
                    "errata_pdf": "b.pdf",
                    "review_pdf": "c.pdf",
                    "text_derivative": "b.txt",
                }
            )
            + "\n",
            encoding="utf-8",
            newline="\n",
        )
        selftest_pdf(root / "citations/c8.pdf")
        selftest_pdf(tmp_dir / "o8.pdf")
        selftest_pdf(tmp_dir / "q8.pdf")
        selftest_pdf(tmp_dir / "q9.pdf")
        manifest_data = read_json(manifest_path)
        manifest_data["entries"].append(
            {
                "filename": "c8.pdf",
                "sha256": stream_sha256(root / "citations/c8.pdf")[0],
                "original_paths": ["tmp/o8.pdf"],
                "source_sha256": stream_sha256(tmp_dir / "o8.pdf")[0],
                "source_id": "C8",
                "bibliographic_metadata": {
                    "title": "T8",
                    "version_label": "VL8",
                    "sha256": bad_sha,
                },
            }
        )
        manifest_path.write_text(
            json.dumps(manifest_data) + "\n", encoding="utf-8", newline="\n"
        )
        q9_sha = stream_sha256(tmp_dir / "q9.pdf")[0]
        with (queue_dir / "completion-work-queue.jsonl").open(
            "a", encoding="utf-8", newline="\n"
        ) as handle:
            handle.write(
                json.dumps(
                    {
                        "source_presentations": [
                            {
                                "source_id": "Q4",
                                "version": "qv",
                                "local_artifact": "tmp/q8.pdf",
                                "bibliographic_identity": {"key": "BQ4", "sha256": bad_sha},
                            },
                            {
                                "source_id": "Q5",
                                "version": "qv5",
                                "artifacts": [{"path": "tmp/q9.pdf", "sha256": q9_sha}],
                                "bibliographic_identity": {"key": "BQ5", "sha256": bad_sha},
                            },
                        ]
                    }
                )
                + "\n"
            )
        (root / "citations/page.html").write_bytes(
            b"<html><body>The header %PDF-1.4 starts a PDF.</body></html>\n"
        )
        (root / "citations/notes.txt").write_bytes(b"starts with %PDF-1.7\n")
        (root / "citations/broken.pdf").write_bytes(b"%PDF-1.4\nbroken\n")

        # Round-9 fixtures: pins nested in sub-dicts or lists that name no
        # file, algorithm/value pairs, hash-describing key words, identity
        # blocks, value conflicts and unreadable queue lines or READMEs.
        r9 = root / "source/references/r9"
        r9_fail = {
            "A": {"path": "a.pdf", "sha256sum": bad_sha},
            "B": {"path": "a.pdf", "expected_sha256": bad_sha},
            "E": {"path": "a.pdf", "integrity": {"sha256": bad_sha}},
            "G": {"path": "a.pdf", "fingerprint": {"algorithm": "SHA-256", "value": bad_sha}},
            "G2": {"path": "a.pdf", "hash_algorithm": "sha256", "value": bad_sha},
            "H": {"path": "a.pdf", "hashes": [{"sha256": bad_sha}]},
            "H2": {"path": "a.pdf", "hashes": [bad_sha]},
            "J": {"path": "a.pdf", "content_sha256": bad_sha},
            "O": {"path": "a.pdf", "body_sha256": bad_sha},
            "V": {"path": "a.pdf", "sha256": None, "verification": {"sha256": bad_sha}},
            "D": {"path": "a.pdf", "notes": {"checks": [{"digest": bad_sha}]}},
            "I": {"source_files": [{"path": "a.pdf", "integrity": {"sha256": bad_sha}}]},
        }
        r9_keep = {
            # A hash of a text selection, and a pin of another (non-held) file.
            "sel": {"path": "a.pdf", "sha256": "GOOD", "reading": [{"selected_text_sha256": bad_sha}]},
            "evid": {"path": "a.pdf", "evidence": [{"path": "notes.md", "sha256": bad_sha}]},
            "pair": {"path": "a.pdf", "fingerprint": {"algorithm": "sha256", "value": "GOOD"}},
            "md5": {"path": "a.pdf", "hashes": [{"algorithm": "md5", "value": "0" * 32}]},
        }
        for name in [*r9_fail, *r9_keep]:
            (r9 / name).mkdir(parents=True)
            selftest_pdf(r9 / name / "a.pdf")
            good = stream_sha256(r9 / name / "a.pdf")[0]
            record = {"source_key": f"R9{name}", "version": "v", **r9_fail.get(name, r9_keep.get(name, {}))}
            (r9 / name / "r.json").write_text(
                json.dumps(record).replace("GOOD", good) + "\n", encoding="utf-8", newline="\n"
            )
        (r9 / "multi").mkdir()
        selftest_pdf(r9 / "multi/a.pdf")
        selftest_pdf(r9 / "multi/b.pdf")
        (r9 / "multi/r.json").write_text(
            json.dumps(
                {
                    "source_key": "R9multi",
                    "source_files": ["a.pdf", "b.pdf"],
                    "integrity": {"sha256": bad_sha},
                }
            )
            + "\n",
            encoding="utf-8",
            newline="\n",
        )
        # Hash containers and algorithm/value pairs fold into the record's
        # plain pins, which bar every held file the record names.
        for name, record in (
            ("fold1", {"hashes": [{"sha256": bad_sha}]}),
            ("fold2", {"fingerprint": {"algorithm": "sha256", "value": bad_sha}}),
        ):
            (r9 / name).mkdir()
            selftest_pdf(r9 / name / "a.pdf")
            selftest_pdf(r9 / name / "b.pdf")
            (r9 / name / "r.json").write_text(
                json.dumps({"source_key": f"R9{name}", "source_files": ["a.pdf", "b.pdf"], **record})
                + "\n",
                encoding="utf-8",
                newline="\n",
            )
        (r9 / "ident").mkdir()
        selftest_pdf(r9 / "ident/a.pdf")
        (r9 / "ident/manifest.json").write_text(
            json.dumps(
                {
                    "source_key": "R9ident",
                    "identity": {"title": "Identity Title", "key": "IdentKey"},
                    "source_files": [{"path": "a.pdf"}],
                }
            )
            + "\n",
            encoding="utf-8",
            newline="\n",
        )
        (r9 / "conf").mkdir()
        selftest_pdf(r9 / "conf/a.pdf")
        for number, version in enumerate(("first", "second")):
            (r9 / f"conf/r{number}.json").write_text(
                json.dumps({"source_key": "R9conf", "version": version, "path": "a.pdf"}) + "\n",
                encoding="utf-8",
                newline="\n",
            )
        (r9 / "conf/README.txt").write_bytes(b"bad \xff\xfe bytes\n")
        for name in ("q9a", "q9b", "q9c", "q9d", "q9e"):
            selftest_pdf(tmp_dir / f"{name}.pdf")
        selftest_pdf(root / "citations/c9.pdf")
        manifest_data = read_json(manifest_path)
        manifest_data["entries"].append(
            {
                "filename": "c9.pdf",
                "sha256": stream_sha256(root / "citations/c9.pdf")[0],
                "source_id": "C9",
                "verification": {"sha256": bad_sha},
            }
        )
        manifest_path.write_text(
            json.dumps(manifest_data) + "\n", encoding="utf-8", newline="\n"
        )
        with (queue_dir / "completion-work-queue.jsonl").open(
            "a", encoding="utf-8", newline="\n"
        ) as handle:
            handle.write("{not json\n")
            handle.write(
                json.dumps(
                    {
                        "source_presentations": [
                            {"source_id": "Q9A", "version": "v", "local_path": "tmp/q9a.pdf", "sha256sum": bad_sha},
                            {"source_id": "Q9B", "version": "v", "local_artifacts": ["tmp/q9b.pdf"], "hashes": [{"sha256": bad_sha}]},
                            {"source_id": "Q9C", "version": "v", "artifacts": [{"path": "tmp/q9c.pdf", "integrity": {"sha256": bad_sha}}]},
                            {"source_id": "Q9D", "version": "v", "local_capture": "tmp/q9d.pdf", "bibliographic_identity": {"key": "x", "checksum": bad_sha}},
                            {"source_id": "Q9E", "version": "v", "artifacts": [{"local_path": "tmp/q9e.pdf", "expected_sha256": bad_sha}]},
                        ]
                    }
                )
                + "\n"
            )

        # Round-10 fixtures: own-file pins under names no path key pairs with
        # the file, further pin spellings, pins of records that name no file
        # themselves, and access-basis fields.
        r10 = root / "source/references/r10"
        r10_fail = {
            "src": {"path": "a.pdf", "source_sha256": bad_sha},
            "orig": {"path": "a.pdf", "original_sha256": bad_sha},
            "doc": {"path": "a.pdf", "document_sha256": bad_sha},
            "ver": {"path": "a.pdf", "verification": {"source_sha256": bad_sha}},
            "art": {"local_artifact": "a.pdf", "artifact_sha256": bad_sha},
            "sha": {"path": "a.pdf", "sha": bad_sha},
            "sha2": {"path": "a.pdf", "SHA2-256": bad_sha},
            "fp": {"path": "a.pdf", "fingerprint": bad_sha},
            "sri": {"path": "a.pdf", "integrity": "sha256-" + bad_sha},
            "meta": {"meta": {"path": "a.pdf"}, "sha256": bad_sha},
        }
        for name, record in r10_fail.items():
            (r10 / name).mkdir(parents=True)
            selftest_pdf(r10 / name / "a.pdf")
            if name == "meta":
                record = {"meta": {"source_key": "R10meta", "title": "T10", **record["meta"]}, "sha256": bad_sha}
            else:
                record = {"source_key": f"R10{name}", "title": "T10", **record}
            (r10 / name / "r.json").write_text(
                json.dumps(record) + "\n", encoding="utf-8", newline="\n"
            )
        (r10 / "meta2").mkdir()
        selftest_pdf(r10 / "meta2/a.pdf")
        selftest_pdf(r10 / "meta2/b.pdf")
        (r10 / "meta2/r.json").write_text(
            json.dumps(
                {
                    "first": {"source_key": "R10meta2", "path": "a.pdf"},
                    "second": {"source_key": "R10meta2b", "path": "b.pdf"},
                    "sha256": bad_sha,
                }
            )
            + "\n",
            encoding="utf-8",
            newline="\n",
        )
        (r10 / "src2").mkdir()
        selftest_pdf(r10 / "src2/a.pdf")
        selftest_pdf(r10 / "src2/b.pdf")
        (r10 / "src2/r.json").write_text(
            json.dumps({"source_key": "R10src2", "local_artifacts": ["a.pdf", "b.pdf"], "source_sha256": bad_sha})
            + "\n",
            encoding="utf-8",
            newline="\n",
        )
        (r10 / "notes").mkdir()
        selftest_pdf(r10 / "notes/a.pdf")
        (r10 / "notes/r.json").write_text(
            json.dumps(
                {
                    "source_key": "R10notes",
                    "path": "a.pdf",
                    "acquisition_method": "direct download",
                    "standing": "authoring draft only",
                    "authoring_standing": "not admitted",
                    "evidence": [{"path": "notes.md", "sha256": bad_sha}],
                }
            )
            + "\n",
            encoding="utf-8",
            newline="\n",
        )
        (r10 / "standing").mkdir()
        selftest_pdf(r10 / "standing/a.pdf")
        (r10 / "standing/r.json").write_text(
            json.dumps(
                {
                    "source_key": "R10standing",
                    "path": "a.pdf",
                    "standing": "authoring draft only",
                    "authoring_standing": "not admitted",
                }
            )
            + "\n",
            encoding="utf-8",
            newline="\n",
        )
        for name in ("o10.pdf", "o10b.pdf", "q10.pdf"):
            selftest_pdf(tmp_dir / name)
        selftest_pdf(root / "citations/c10.pdf")
        selftest_pdf(root / "citations/c10b.pdf")
        manifest_data = read_json(manifest_path)
        manifest_data["entries"].extend(
            [
                {"original_paths": ["tmp/o10.pdf"], "original_sha256": bad_sha, "source_id": "C10", "title": "T10"},
                {
                    "filename": "c10.pdf",
                    "sha256": stream_sha256(root / "citations/c10.pdf")[0],
                    "original_paths": ["tmp/o10b.pdf"],
                    "original_paths_sha256": bad_sha,
                    "source_id": "C10b",
                    "title": "T10",
                },
                {
                    "filename": "c10b.pdf",
                    "sha256": stream_sha256(root / "citations/c10b.pdf")[0],
                    "source_id": "C10c",
                    "bibliographic_metadata": {"title": "T10c", "sha256": bad_sha},
                },
            ]
        )
        manifest_path.write_text(
            json.dumps(manifest_data) + "\n", encoding="utf-8", newline="\n"
        )
        with (queue_dir / "completion-work-queue.jsonl").open(
            "a", encoding="utf-8", newline="\n"
        ) as handle:
            handle.write(
                json.dumps(
                    {
                        "source_presentations": [
                            {
                                "source_id": "Q10",
                                "title": "T10",
                                "local_artifact": "tmp/q10.pdf",
                                "artifact_sha256": bad_sha,
                            },
                            {
                                "source_id": "Q10md",
                                "artifacts": [{"path": "tmp/notes10.md", "sha256": bad_sha}],
                            },
                        ]
                    }
                )
                + "\n"
            )

        data, stats = build_index(root)
        entries = {entry["path"]: entry for entry in data["entries"]}
        for name in r10_fail:
            path = f"source/references/r10/{name}/a.pdf"
            entry = entries[path]
            assert entry["source_ids"] == [] and entry["bibkeys"] == [], (path, entry)
            assert entry["titles"] == [], (path, entry)
            assert any(f"{path} " in item for item in stats.sha_mismatches), path
            assert f"R10{name}" not in data["source_index"], name
        assert "R10src2" not in data["source_index"]
        for name in ("a.pdf", "b.pdf"):
            path = f"source/references/r10/src2/{name}"
            assert any(f"{path} " in item for item in stats.sha_mismatches), path
        assert data["source_index"]["R10meta2"] == ["source/references/r10/meta2/a.pdf"]
        assert any(
            "r10/meta2/r.json" in item and "sha256" in item for item in stats.unpaired_pins
        ), stats.unpaired_pins
        notes = entries["source/references/r10/notes/a.pdf"]
        assert notes["source_ids"] == ["R10notes"] and notes["access_basis"] == "direct download", notes
        assert not any("r10/notes" in item for item in stats.unpaired_pins + stats.sha_mismatches)
        assert entries["source/references/r10/standing/a.pdf"]["access_basis"] is None
        for path in ("tmp/o10.pdf", "tmp/o10b.pdf", "citations/c10.pdf"):
            entry = entries[path]
            assert entry["source_ids"] == [] and entry["titles"] == [], (path, entry)
            assert any(f"{path} " in item for item in stats.sha_mismatches), path
        assert "C10" not in data["source_index"] and "C10b" not in data["source_index"]
        assert any(
            "citations/manifest.json:" in item and "bibliographic_metadata.sha256" in item
            and "names no held file" in item
            for item in stats.unpaired_pins
        ), stats.unpaired_pins
        q10 = entries["tmp/q10.pdf"]
        assert q10["source_ids"] == [] and q10["titles"] == [], q10
        assert any("tmp/q10.pdf " in item for item in stats.sha_mismatches)
        assert not any("notes10.md" in item or "Q10md" in item for item in stats.unpaired_pins)
        assert recorded_pin("sha256-" + bad_sha) == bad_sha
        assert build_exit_code(BuildStats(unpaired_pins=["x"]), strict=False) == 0
        assert build_exit_code(BuildStats(unpaired_pins=["x"]), strict=True) == 1
        assert build_exit_code(BuildStats(sha_mismatches=["x"]), strict=False) == 1
        for name in r9_fail:
            path = f"source/references/r9/{name}/a.pdf"
            entry = entries[path]
            assert entry["source_ids"] == [] and entry["version"] is None, (path, entry)
            assert any(f"{path} " in item for item in stats.sha_mismatches), path
            assert f"R9{name}" not in data["source_index"], name
        for name in r9_keep:
            path = f"source/references/r9/{name}/a.pdf"
            assert data["source_index"][f"R9{name}"] == [path], name
            assert not any(f"{path} " in item for item in stats.sha_mismatches), name
        assert any(
            "r9/sel/r.json" in item and "selected_text_sha256" in item for item in stats.unpaired_pins
        ), stats.unpaired_pins
        assert data["source_index"]["R9multi"] == [
            "source/references/r9/multi/a.pdf",
            "source/references/r9/multi/b.pdf",
        ]
        assert any(
            "r9/multi/r.json" in item and "integrity.sha256" in item for item in stats.unpaired_pins
        ), stats.unpaired_pins
        for name in ("fold1", "fold2"):
            assert f"R9{name}" not in data["source_index"], name
            for file_name in ("a.pdf", "b.pdf"):
                path = f"source/references/r9/{name}/{file_name}"
                assert any(f"{path} " in item for item in stats.sha_mismatches), path
        ident = entries["source/references/r9/ident/a.pdf"]
        assert ident["titles"] == ["Identity Title"] and "IdentKey" in ident["bibkeys"], ident
        conf = entries["source/references/r9/conf/a.pdf"]
        assert conf["version"] is None and conf["source_ids"] == ["R9conf"], conf
        assert any("r9/conf/a.pdf" in item for item in stats.value_conflicts["version"])
        assert any("r9/conf/README.txt" in item for item in stats.unreadable_json)
        assert any("completion-work-queue.jsonl:line" in item for item in stats.unreadable_json)
        for name in ("q9a", "q9b", "q9c", "q9d", "q9e"):
            entry = entries[f"tmp/{name}.pdf"]
            assert entry["source_ids"] == [] and entry["version"] is None, (name, entry)
            assert any(f"tmp/{name}.pdf " in item for item in stats.sha_mismatches), name
            assert name.upper() not in data["source_index"], name
        assert "C9" not in data["source_index"]
        assert entries["citations/c9.pdf"]["source_ids"] == []
        assert any(
            "citations/c9.pdf " in item and "verification.sha256" in item
            for item in stats.sha_mismatches
        ), stats.sha_mismatches
        r9_summary = summary_lines(data, stats, root / "tmp/out.json", False)
        conflicts = len(stats.value_conflicts["version"])
        assert f"version_conflicts: {conflicts}" in r9_summary, r9_summary
        assert any("version source/references/r9/conf/a.pdf: " in line for line in r9_summary)
        assert any(line.startswith("unreadable_records: ") for line in r9_summary)
        for name in r8_fail:
            file_name = "b.txt" if name == "S3text" else "a.pdf"
            path = f"source/references/r8/{name}/{file_name}"
            entry = entries[path]
            assert entry["source_ids"] == [] and entry["version"] is None, (path, entry)
            assert any(f"{path} " in item for item in stats.sha_mismatches), path
        for name in ("S10", "S1", "S2hex", "S2hash", "S2checksum", "S2files", "S2nested"):
            assert name not in data["source_index"], name
        assert data["source_index"]["S3text"] == ["source/references/r8/S3text/a.pdf"]
        for name in r8_keep:
            path = f"source/references/r8/{name}/a.pdf"
            assert data["source_index"][name] == [path], name
            assert entries[path]["version"] == f"v-{name}", name
            assert not any(f"{path} " in item for item in stats.sha_mismatches), name
        assert any(
            "r8/S2layout/r.json" in item and "layout_sha256" in item
            for item in stats.unpaired_pins
        ), stats.unpaired_pins
        assert data["source_index"]["S6"] == ["source/references/r8/S6/a.pdf"]
        assert entries["source/references/r8/S6/a.pdf"]["version"] == "v6"
        for name in ("b.pdf", "c.pdf", "b.txt"):
            entry = entries[f"source/references/r8/S6/{name}"]
            assert entry["source_ids"] == [] and entry["version"] is None, (name, entry)
            assert entry["bibkeys"] == [] and entry["titles"] == [], (name, entry)
            assert any("r8/S6/r.json:" in item for item in entry["evidence"]), (name, entry)
        for path in ("citations/c8.pdf", "tmp/o8.pdf"):
            entry = entries[path]
            assert "T8" not in entry["titles"] and entry["version"] is None, (path, entry)
            assert entry["source_ids"] == [], (path, entry)
            assert any(f"{path} " in item for item in stats.sha_mismatches), path
        assert "C8" not in data["source_index"]
        for path, source_id in (("tmp/q8.pdf", "Q4"), ("tmp/q9.pdf", "Q5")):
            entry = entries[path]
            assert entry["source_ids"] == [] and entry["version"] is None, (path, entry)
            assert any(f"{path} " in item for item in stats.sha_mismatches), path
            assert source_id not in data["source_index"], source_id
        assert entries["citations/page.html"]["kind"] == "html"
        assert entries["citations/notes.txt"]["kind"] == "txt"
        assert entries["citations/page.html"]["pdf_pages"] is None
        assert entries["citations/broken.pdf"]["kind"] == "pdf"
        assert kind_for(Path("n.txt"), b"notes\n%PDF-1.7\n") == "txt"
        assert kind_for(Path("x.bin"), b"\xef\xbb\xbf\x00 %PDF-1.4\n") == "pdf"
        quiet = io.StringIO()
        with contextlib.redirect_stderr(quiet):
            assert pdf_page_count(root / "citations/broken.pdf") is None
            assert pdf_page_count(root / "citations/page.html") is None
        assert quiet.getvalue() == "", quiet.getvalue()
        challenge = entries["source/references/r7/challenge.pdf"]
        assert challenge["kind"] == "html" and challenge["pdf_pages"] is None, challenge
        junk = entries["source/references/r7/junk.pdf"]
        assert junk["kind"] == "other" and junk["pdf_pages"] is None, junk
        assert entries["source/references/r7/prefixed.pdf"]["kind"] == "pdf"
        for name in r7_fail:
            path = f"source/references/r7/{name}/a.pdf"
            entry = entries[path]
            assert entry["source_ids"] == [] and entry["bibkeys"] == [], (path, entry)
            assert entry["version"] is None, (path, entry)
            assert any(f"{path} " in item for item in stats.sha_mismatches), path
            assert f"R7{name}" not in data["source_index"], name
        assert data["source_index"]["R7ok1"] == ["source/references/r7/ok1/a.pdf"]
        assert data["source_index"]["R7unpaired"] == ["source/references/r7/unpaired/a.pdf"]
        assert any(
            "r7/unpaired/r.json" in item and "extraction_sha256" in item
            for item in stats.unpaired_pins
        ), stats.unpaired_pins
        assert not any("r7/ok1" in item for item in stats.sha_mismatches + stats.unpaired_pins)
        tmp_ref = entries["tmp/r7-preview.pdf"]
        assert tmp_ref["source_ids"] == ["R7tmp"] and tmp_ref["location_stable"] is False
        assert "source/references/r7/tmpref.json:local_path" in tmp_ref["evidence"]
        assert entries["tmp/r7-t2.pdf"]["source_ids"] == []
        assert "R7tmpbad" not in data["source_index"]
        assert named_sha_keys("artifacts")[:2] == ["artifacts_sha256", "artifact_sha256"]
        assert normal_key("SHA-256") == "sha256"
        assert kind_for(Path("x.pdf"), b"<html>") == "html"
        for name, files in r6_fail_files.items():
            for file_name in files:
                path = f"source/references/r6/{name}/{file_name}"
                entry = entries[path]
                assert entry["source_ids"] == [], (path, entry)
                assert entry["bibkeys"] == [], (path, entry)
                assert entry["version"] is None, (path, entry)
                assert any(f"{path} " in item for item in stats.sha_mismatches), path
            assert f"R6{name}" not in data["source_index"], name
        for name in ("q6.pdf", "q7.pdf"):
            assert entries[f"tmp/{name}"]["source_ids"] == [], name
            assert entries[f"tmp/{name}"]["version"] is None, name
            assert any(f"tmp/{name} " in item for item in stats.sha_mismatches), name
        assert "R6Q6" not in data["source_index"]
        assert "R6Q7" not in data["source_index"]
        assert not any("source/references/r6/ok" in item for item in stats.sha_mismatches)
        # A derived file is indexed with evidence but takes no identity.
        assert data["source_index"]["R6OK"] == ["source/references/r6/ok/a.pdf"]
        assert entries["source/references/r6/ok/a.pdf"]["version"] == "v-ok"
        derived = entries["source/references/r6/ok/b.txt"]
        assert derived["source_ids"] == [] and derived["version"] is None, derived
        assert "source/references/r6/ok/r.json:derived_file" in derived["evidence"]
        dep = entries["source/references/r6/okdep/a.pdf"]
        assert dep["source_ids"] == [] and dep["version"] is None, dep
        assert "source/references/r6/okdep/r.json:dependency_pdf" in dep["evidence"]
        # Neither scan_image nor text_path is the record's own file: no identity.
        assert "R6OK3" not in data["source_index"]
        for name in ("a.pdf", "b.txt"):
            ok3 = entries[f"source/references/r6/ok3/{name}"]
            assert any("r6/ok3/r.json:" in item for item in ok3["evidence"]), ok3
        assert entries["source/references/r6/F13/a.pdf"]["source_ids"] == []
        assert entries["source/references/r6/F13/a.pdf"]["bibkeys"] == []
        assert "pdf-blob" not in data["source_index"]
        assert data["source_index"]["R6KEY"] == ["source/references/r6/okkey/a.pdf"]
        assert recorded_pin("sha256:" + "A" * 64) == "a" * 64
        assert recorded_pin(None) is None and recorded_pin(True) is None
        assert recorded_pin({"sha256": "a" * 64}) == MALFORMED_PIN
        assert stem_sha_keys("failed_response_artifact") == [
            "failed_response_sha256",
            "response_sha256",
        ]
        for name in ("a.pdf", "b.pdf", "c.pdf", "e.html", "f.pdf"):
            entry = entries[f"source/references/adv5/{name}"]
            assert entry["source_ids"] == [], (name, entry)
            assert entry["bibkeys"] == [], (name, entry)
            assert entry["version"] is None, (name, entry)
            assert any(f"adv5/{name} recorded" in item for item in stats.sha_mismatches), name
        for key in ("KA", "KB", "KC", "KE", "KF"):
            assert key not in data["source_index"], key
        data_pdf = entries["source/references/adv5/data.pdf"]
        assert "source/references/adv5/README.md:text reference" in data_pdf["evidence"]
        assert not any("mentions a.pdf" in item for item in entries["source/references/adv5/a.pdf"]["evidence"])
        assert not any("adv5/README.md" in item for item in stats.missing_named_paths)
        for name in ("spaced name.pdf", "bare spaced (1).pdf"):
            spaced = entries[f"source/references/adv5/{name}"]
            assert "source/references/adv5/README.md:text reference" in spaced["evidence"]
        gone = [item for item in stats.missing_named_paths if "gone.pdf" in item]
        assert gone == ["source/references/adv5/M.json:local_path: gone.pdf"], gone
        assert len(stats.missing_named_paths) == len(set(stats.missing_named_paths))
        assert "ORIG" in entries["tmp/orig.pdf"]["source_ids"]
        assert any(
            item.startswith("citations/manifest.json:") and "original_paths" in item
            for item in entries["tmp/orig.pdf"]["evidence"]
        )
        assert entries["tmp/bad-orig.pdf"]["source_ids"] == []
        assert "tmp/bad-orig.pdf" not in data["source_index"].get("BADORIG", [])
        assert any("tmp/bad-orig.pdf recorded" in item for item in stats.sha_mismatches)
        assert "citations/demo.pdf" in entries
        assert "citations/a.pdf" in entries
        assert "citations/c.pdf" in entries
        assert "source/references/demo/demo.txt" in entries
        assert "source/references/demo/figure.png" in entries
        assert "source/references/demo/other.pdf" in entries
        assert "source/references/demo/z1/resp.html" in entries
        assert "source/references/demo/z2/resp.html" in entries
        assert "tmp/q.pdf" in entries
        assert "tmp/b.pdf" in entries
        assert "tmp/c.pdf" in entries
        assert "tmp/d.pdf" in entries
        assert "source/references/adv/a.pdf" in entries
        assert "source/references/adv3/a.pdf" in entries
        assert "source/references/adv4/b.pdf" in entries
        assert entries["citations/demo.pdf"]["sha256"] == pdf_sha
        assert entries["citations/demo.pdf"]["bytes"] == pdf_bytes
        assert entries["citations/demo.pdf"]["kind"] == "pdf"
        if entries["citations/demo.pdf"]["pdf_pages"] is not None:
            assert entries["citations/demo.pdf"]["pdf_pages"] == 1
        assert "SRC-TEST" in entries["citations/demo.pdf"]["source_ids"]
        assert "DemoBib" in entries["citations/demo.pdf"]["bibkeys"]
        assert "Demo Paper" in entries["citations/demo.pdf"]["titles"]
        assert "Demo Presentation" in entries["citations/demo.pdf"]["titles"]
        assert data["source_index"]["SRC-TEST"] == ["citations/demo.pdf"]
        assert entries["source/references/demo/demo.txt"]["extent_verified"] is True
        assert "SRC-Q" in entries["tmp/q.pdf"]["source_ids"]
        assert data["source_index"]["SRC-Q"] == ["tmp/q.pdf"]
        assert entries["tmp/q.pdf"]["location_stable"] is False
        assert "Work Unit Title" not in entries["citations/demo.pdf"]["titles"]
        assert "Work Unit Title" not in entries["tmp/q.pdf"]["titles"]
        assert "KeyY" not in entries["source/references/demo/other.pdf"]["source_ids"]
        assert entries["source/references/demo/other.pdf"]["version"] is None
        assert entries["source/references/demo/other.pdf"]["extent_verified"] is None
        assert "KeyZ1" in entries["source/references/demo/z1/resp.html"]["source_ids"]
        assert entries["source/references/demo/z2/resp.html"]["source_ids"] == []
        assert entries["citations/a.pdf"]["source_ids"] == []
        assert entries["citations/a.pdf"]["version"] is None
        assert entries["citations/a.pdf"]["extent_verified"] is None
        assert entries["citations/c.pdf"]["source_ids"] == []
        assert entries["citations/c.pdf"]["version"] is None
        assert "K1" not in entries["source/references/adv/a.pdf"]["source_ids"]
        assert "K1" not in entries["source/references/adv/a.pdf"]["bibkeys"]
        assert entries["source/references/adv/a.pdf"]["version"] is None
        assert entries["source/references/adv3/a.pdf"]["source_ids"] == []
        assert entries["source/references/adv3/a.pdf"]["bibkeys"] == []
        assert entries["source/references/adv3/a.pdf"]["version"] is None
        assert entries["source/references/adv4/b.pdf"]["source_ids"] == []
        assert entries["source/references/adv4/b.pdf"]["bibkeys"] == []
        assert entries["source/references/adv4/b.pdf"]["version"] is None
        assert entries["tmp/b.pdf"]["source_ids"] == []
        assert entries["tmp/b.pdf"]["version"] is None
        assert entries["tmp/b.pdf"]["titles"] == []
        assert entries["tmp/c.pdf"]["source_ids"] == []
        assert entries["tmp/c.pdf"]["version"] is None
        assert entries["tmp/d.pdf"]["source_ids"] == []
        assert entries["tmp/d.pdf"]["version"] is None
        assert "Q1" not in data["source_index"]
        assert "Q2" not in data["source_index"]
        assert "Q3" not in data["source_index"]
        assert "K1" not in data["source_index"]
        assert "K2" not in data["source_index"]
        assert "C4" not in data["source_index"]
        assert stats.sha_mismatches
        summary = summary_lines(
            data,
            stats,
            root / "spec/coverage/edition-2026/held-sources.json",
            False,
        )
        assert "recorded_sha_mismatch_details:" in summary
        assert any("citations/a.pdf" in line for line in summary)
        assert any("citations/c.pdf" in line for line in summary)
        assert any("source/references/adv/a.pdf" in line for line in summary)
        assert any("source/references/adv3/a.pdf" in line for line in summary)
        assert any("source/references/adv4/b.pdf" in line for line in summary)
        assert any("tmp/b.pdf" in line for line in summary)
        assert any("tmp/c.pdf" in line for line in summary)
        assert any("tmp/d.pdf" in line for line in summary)
        assert lookup(data, "SRC-TEST", root)[0]["path"] == "citations/demo.pdf"
        assert lookup(data, "source/references/demo/demo.txt", root)[0]["sha256"] == text_sha
        assert validate_out_path(root / "spec/coverage/edition-2026/held-sources.json", root) is None
        assert validate_out_path(root / "citations/q.pdf", root)
        non_index = root / "tmp/not-held.json"
        non_index.write_text("{}", encoding="utf-8", newline="\n")
        assert validate_out_path(non_index, root)
        held_index = root / "tmp/existing-held.json"
        held_index.write_text(
            json.dumps({"entries": [], "source_index": {}}) + "\n",
            encoding="utf-8",
            newline="\n",
        )
        assert validate_out_path(held_index, root) is None
    print("selftest passed")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--selftest", action="store_true", help="run temp-fixture checks")
    subparsers = parser.add_subparsers(dest="command")

    build = subparsers.add_parser("build", help="build the held-source index")
    build.add_argument("--out", default=str(DEFAULT_OUT), help="output JSON path")
    build.add_argument("--apply", action="store_true", help="write the output JSON")
    build.add_argument(
        "--strict", action="store_true", help="exit 1 when any recorded pin is unpaired"
    )
    build.set_defaults(func=run_build)

    lookup_parser = subparsers.add_parser("lookup", help="look up a source id or path")
    lookup_parser.add_argument("query")
    lookup_parser.set_defaults(func=run_lookup)
    return parser


def main(argv: list[str] | None = None) -> int:
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8")
    parser = build_parser()
    args = parser.parse_args(argv)
    if args.selftest:
        run_selftest()
        return 0
    if not hasattr(args, "func"):
        parser.print_usage(sys.stderr)
        return 2
    return int(args.func(args))


if __name__ == "__main__":
    raise SystemExit(main())
