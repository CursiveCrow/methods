"""Exact, local compatibility aliases for reviewed handbook label migrations.

This module does not relax the label taxonomy or inherited-source provenance.
Only a complete, valid manifest/command match yields any registered aliases.
"""
from __future__ import annotations

import json
from pathlib import Path
import re


KINDS = {
    "hblemma-argument": "thm:",
    "annexlemma-label": "thm:",
    "section-label": "sec:",
}
LABEL = re.compile(r"[A-Za-z][A-Za-z0-9._-]*:[A-Za-z0-9][A-Za-z0-9._:-]*\Z")
CANONICAL = re.compile(r"(?:thm|sec):[A-Za-z0-9][A-Za-z0-9._-]*\Z")
FILE = re.compile(r"handbook/(?:parts|annex)/p[0-9]{2}/[A-Za-z0-9._/-]+\.tex\Z")
ALIAS = re.compile(r"\\hblegacylabel(?![A-Za-z@])")
PLAIN_LABEL = re.compile(r"\\label\s*\{([^{}]+)\}")


def _unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key {key!r}")
        result[key] = value
    return result


def load_legacy_label_policy(path: Path):
    """Reject missing, malformed, and duplicate-key policy documents."""
    try:
        return json.loads(path.read_text(encoding="utf-8-sig"),
                          object_pairs_hook=_unique_object)
    except (OSError, ValueError) as exc:
        raise ValueError(f"cannot read {path}: {exc}") from exc


def _optional_title_end(body: str, pos: int) -> int | None:
    """The annexlemma optional title, with grouped/escaped brackets respected."""
    while pos < len(body) and body[pos].isspace():
        pos += 1
    if pos >= len(body) or body[pos] != "[":
        return pos
    braces = 0
    pos += 1
    while pos < len(body):
        char = body[pos]
        if char == "\\":
            pos += 2
            continue
        if char == "{":
            braces += 1
        elif char == "}":
            braces -= 1
            if braces < 0:
                return None
        elif char == "]" and braces == 0:
            return pos + 1
        pos += 1
    return None


def _canonical_ends(body, canonical, kind, read_args):
    """Require the declared kind, not merely a nearby occurrence of its name."""
    if kind == "hblemma-argument":
        for match in re.finditer(r"\\begin\{hblemma\}", body):
            args, end = read_args(body, match.end(), 3)
            if len(args) == 3 and args[0] == canonical:
                yield end
        return
    for label in PLAIN_LABEL.finditer(body):
        if label.group(1) != canonical:
            continue
        if kind == "annexlemma-label":
            headers = re.finditer(r"\\begin\{annexlemma\}", body[:label.start()])
            for header in headers:
                end = _optional_title_end(body, header.end())
                if end is not None and not body[end:label.start()].strip():
                    yield label.end()
        elif kind == "section-label":
            for header in re.finditer(r"\\section(?![A-Za-z@*])", body[:label.start()]):
                args, end = read_args(body, header.end(), 1)
                if len(args) == 1 and not body[end:label.start()].strip():
                    yield label.end()


def validate_legacy_labels(policy, bodies, label_sites, read_args):
    """Return (errors, aliases) for comment/verbatim-stripped handbook texts.

Each accepted alias is (old, canonical, location). The caller must register
these only after this function returns; label_sites must contain ordinary
definitions only, so an old spelling cannot be laundered as a new definition.
The caller's normal scanner remains authoritative for duplicate definitions.
"""
    errors = []
    rows = []
    if not isinstance(policy, dict) or set(policy) != {"schema_version", "aliases"}:
        errors.append("policy requires exactly schema_version and aliases")
    elif type(policy["schema_version"]) is not int or policy["schema_version"] != 1:
        errors.append("policy schema_version must be 1")
    elif not isinstance(policy["aliases"], list):
        errors.append("policy aliases must be an array")
    else:
        for index, row in enumerate(policy["aliases"], 1):
            where = f"policy alias {index}"
            if not isinstance(row, dict) or set(row) != {"old", "canonical", "file", "kind"}:
                errors.append(f"{where}: requires exactly old/canonical/file/kind")
                continue
            if any(not isinstance(value, str) or not value for value in row.values()):
                errors.append(f"{where}: fields must be nonempty literal strings")
                continue
            old, canonical, file, kind = (row[k] for k in ("old", "canonical", "file", "kind"))
            if not LABEL.fullmatch(old) or old == canonical:
                errors.append(f"{where}: invalid old label {old!r}")
            if kind not in KINDS or not CANONICAL.fullmatch(canonical) or not canonical.startswith(KINDS.get(kind, "!")):
                errors.append(f"{where}: invalid canonical label/kind {canonical!r}/{kind!r}")
            if not FILE.fullmatch(file) or any(p in {".", "..", ""} for p in file.split("/")):
                errors.append(f"{where}: invalid editorial file {file!r}")
            if kind != "hblemma-argument" and not file.startswith("handbook/annex/"):
                errors.append(f"{where}: {kind} must be in an annex file")
            rows.append(row)

    old_counts = {}
    target_counts = {}
    for row in rows:
        old_counts[row["old"]] = old_counts.get(row["old"], 0) + 1
        target_counts[row["canonical"]] = target_counts.get(row["canonical"], 0) + 1
    for old, count in old_counts.items():
        if count != 1:
            errors.append(f"policy repeats old label {old!r}")
    for canonical, count in target_counts.items():
        if count != 1:
            errors.append(f"policy repeats canonical label {canonical!r}")
        if canonical in old_counts:
            errors.append(f"alias chain/cycle through {canonical!r} is forbidden")

    actual = {}
    for relative, body in bodies.items():
        for match in ALIAS.finditer(body):
            location = f"{relative}:{body.count(chr(10), 0, match.start()) + 1}"
            args, _ = read_args(body, match.end(), 2)
            if len(args) != 2 or any(not LABEL.fullmatch(arg) for arg in args):
                errors.append(f"malformed hblegacylabel declaration ({location})")
                continue
            old, canonical = args
            actual.setdefault(old, []).append((canonical, relative, match.start(), location))

    expected = {row["old"]: row for row in rows}
    for old in sorted(set(actual) - set(expected)):
        errors.append(f"unmanifested alias {old!r} ({actual[old][0][3]})")

    accepted = []
    for old, row in expected.items():
        canonical = row["canonical"]
        relative = row["file"].removeprefix("handbook/")
        declarations = actual.get(old, [])
        if len(declarations) != 1:
            errors.append(f"{old!r}: expected one declaration, found {len(declarations)}")
            continue
        target, actual_relative, pos, location = declarations[0]
        if target != canonical or actual_relative != relative:
            errors.append(f"{old!r}: declaration target/file disagrees with policy ({location})")
            continue
        if old in label_sites:
            errors.append(f"{old!r}: old spelling is also an ordinary/environment label definition")
        sites = label_sites.get(canonical, [])
        if len(sites) != 1 or not sites[0].startswith(relative + ":"):
            errors.append(f"{old!r}: canonical definition must be globally unique in {relative}")
        ends = list(_canonical_ends(bodies[relative], canonical, row["kind"], read_args))
        if len(ends) != 1 or ends[0] > pos or bodies[relative][ends[0]:pos].strip():
            errors.append(f"{old!r}: alias must immediately follow its {row['kind']} canonical definition ({location})")
        accepted.append((old, canonical, location))

    # An invalid manifest/command set grants no aliases, even if some rows fit.
    return errors, [] if errors else accepted
