#!/usr/bin/env python3
"""Join every active inherited source unit to its interval-audit evidence.

This is an administrative crosswalk, not a content or provenance verdict.
Every unit remains open until later reviewer-supplied data passes exact identity,
restoration-record, wrapper-reachability, destination, label, completeness,
audit-result, and recorded-evidence checks.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import re
import unicodedata
from pathlib import Path, PurePosixPath

if __package__:
    from . import check_inherited_restoration as inherited_restoration
else:
    import check_inherited_restoration as inherited_restoration


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INVENTORY = ROOT / "spec/source-unit-inventory.csv"
DEFAULT_AUDIT_MAP = ROOT / "spec/inherited-source-map.csv"
DEFAULT_SOURCE = ROOT / "source/formal-logic-reference.tex"
DEFAULT_CSV = ROOT / "spec/source-unit-audit-crosswalk.csv"
DEFAULT_MD = ROOT / "spec/source-unit-audit-crosswalk.md"
DEFAULT_REVIEWED_RECORDS = (
    ROOT / "spec/provenance/reviewed-source-unit-records.json"
)

AUTHORITY_PATH = "source/formal-logic-reference.tex"
AUTHORITY_SHA256 = (
    "0509750c13b88a4e18914bd52bde171c725cba14221cbfc2227d7693a2b421cc"
)
AUTHORITY_EDITION = "Version 1.0"
REVIEW_SCHEMA_VERSION = 5
OPEN_DISPOSITION = "open/missing"
PASSING_DISPOSITION = "full transcription"
CORRECTED_DISPOSITION = "full reconstruction"
CORRECTED_AUDIT_RESULT = "corrected-and-verified"
TERMINAL_DISPOSITIONS = {PASSING_DISPOSITION, CORRECTED_DISPOSITION}
PERMITTED_DISPOSITIONS = {OPEN_DISPOSITION, *TERMINAL_DISPOSITIONS}
RESULT_VALUES = {"pass", "fail", "pending"}
PENDING_AUDIT_RESULT = "pending/unclassified"
EXACT_AUDIT_RESULTS = ("full-and-accurate", "layout-only relocation")
PASSING_AUDIT_RESULTS = (*EXACT_AUDIT_RESULTS, CORRECTED_AUDIT_RESULT)
AUDIT_RESULTS = (PENDING_AUDIT_RESULT, *PASSING_AUDIT_RESULTS)
DEFECT_EXCLUSIONS = (
    "altered",
    "abridged",
    "omitted",
    "hybridized",
    "unsupported addition",
)
CORRECTED_DEFECT_EXCLUSIONS = ("unexplained alteration", *DEFECT_EXCLUSIONS[1:])
CORRECTION_SNAPSHOT_FIELDS = (
    "unit_ordinal", "source_sha256", "restoration_provenance_id",
    "restoration_record_sha256", "presentation_identity_value",
    "handbook_destination", "handbook_destination_sha256",
)
LAYOUT_CHANGES = (
    "wrapper",
    "placement",
    "pagination",
    "typography",
    "stable label",
    "added navigation heading",
)

COMPLETENESS_FIELDS = (
    "notation",
    "definitions",
    "rules",
    "side_conditions",
    "hypotheses",
    "statements",
    "proofs",
    "examples",
    "qualifications",
    "attribution",
)
VERIFICATION_FIELDS = (
    "source_fidelity_ai",
    "topic_specialist_ai",
    "adversarial_publication_ai",
    "static",
    "build",
    "visual",
)
AI_REVIEW_FIELDS = VERIFICATION_FIELDS[:3]
VERIFICATION_OUTPUT_FIELDS = {
    field: f"{field}_verification" for field in VERIFICATION_FIELDS
}

REVIEW_RECORD_FIELDS = {
    "unit_ordinal",
    "unit_kind",
    "unit_title",
    "unit_source_label",
    "source_start",
    "source_end",
    "source_sha256",
    "restoration_record_path",
    "restoration_record_sha256",
    "restoration_provenance_id",
    "authority_path",
    "authority_sha256",
    "authority_edition_status",
    "authority_edition_value",
    "presentation_identity_status",
    "presentation_identity_value",
    "presentation_identity_description",
    "provenance_disposition",
    "handbook_destination_status",
    "handbook_destination",
    "handbook_destination_sha256",
    "stable_labels",
    "audit_result",
    "layout_changes",
    "defect_exclusions",
    "variant_links",
    "completeness",
    "verification",
    "verification_evidence",
}
EVIDENCE_FIELDS = {
    "category",
    "recorded_result",
    "artifact_path",
    "sha256",
    "producer_identity",
    "recorded_scope",
}
AI_EVIDENCE_FIELDS = EVIDENCE_FIELDS | {
    "model",
    "model_version",
    "instructions",
    "consulted_authorities",
    "findings",
    "other_review_outputs_consulted",
}
CONSULTED_AUTHORITY_FIELDS = {"path", "locator", "sha256"}
VARIANT_LINK_FIELDS = {
    "unit_ordinal",
    "unit_source_label",
    "source_start",
    "source_end",
    "source_sha256",
    "relationship",
}
SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
LABEL_RE = re.compile(
    r"^(?:part|ch|sec|entry|def|thm|lem|cor|method|rem|prob|app|ex|tab|fig|sheet|rule|annex):"
    r"[A-Za-z0-9][A-Za-z0-9._-]*$"
)
UNIT_LABEL_RE = re.compile(
    r"^(?:part|ch|sec|entry|def|thm|lem|cor|method|rem|prob|app|ex|tab|fig|annex):"
    r"[A-Za-z0-9][A-Za-z0-9._-]*$"
)
PART_CONTENT_DESTINATION_RE = re.compile(
    r"^handbook/parts/p(?P<number>[0-9]{2})/.+\.tex$"
)
PART_DRIVER_DESTINATION_RE = re.compile(
    r"^handbook/parts/p(?P<number>[0-9]{2})\.tex$"
)
ANNEX_CONTENT_DESTINATION_RE = re.compile(
    r"^handbook/annex/p(?P<number>[0-9]{2})/.+\.tex$"
)
RESTORATION_DESTINATION_RE = re.compile(r"^handbook/restoration/.+\.tex$")
FRONTMATTER_DESTINATION = "handbook/frontmatter.tex"
RESTORATION_PROVENANCE_ID_RE = re.compile(
    r"^(?:PRE|SRC|CTL|SEP)-[0-9]{5}-[0-9]{5}$"
)
RESTORATION_RECORD_PATH_RE = re.compile(
    r"^spec/provenance/(?P<provenance_id>"
    r"(?:PRE|SRC|CTL|SEP)-[0-9]{5}-[0-9]{5})\.json$"
)
STATIC_TEX_INPUT_RE = re.compile(
    r"\\input(?![A-Za-z@])\s*(?:\{([^{}]+)\}|([^\s%{}]+))"
)
FORBIDDEN_LOOKUP_DESTINATIONS = {
    "handbook/parts/p01/symbol-registry.tex",
    "handbook/parts/p14/master-tables.tex",
    "handbook/parts/p14/rule-sheets.tex",
}
LABEL_OWNER_ENVIRONMENTS = (
    "hbtheorem",
    "hblemma",
    "hbcorollary",
    "hbdefinition",
    "hbconvention",
    "hbmethod",
    "hbexample",
    "hbwarning",
    "proofboundary",
    "systementry",
    "annexitem",
)


class DuplicateJsonFieldError(ValueError):
    """A duplicate name made a reviewer-supplied JSON object ambiguous."""

OUTPUT_FIELDS = (
    "unit_ordinal",
    "unit_kind",
    "unit_title",
    "unit_source_label",
    "source_start",
    "source_end",
    "source_sha256",
    "restoration_provenance_id",
    "restoration_record_path",
    "restoration_record_sha256",
    "authority_path",
    "authority_sha256",
    "authority_edition_status",
    "authority_edition_value",
    "presentation_identity_status",
    "presentation_identity_value",
    "presentation_identity_description",
    "audit_interval_ids",
    "audit_class_evidence",
    "provenance_disposition",
    "handbook_destination_status",
    "handbook_destination",
    "stable_labels",
    "audit_result",
    "notation_completeness",
    "definitions_completeness",
    "rules_completeness",
    "side_conditions_completeness",
    "hypotheses_completeness",
    "statements_completeness",
    "proofs_completeness",
    "examples_completeness",
    "qualifications_completeness",
    "attribution_completeness",
    "source_fidelity_ai_verification",
    "topic_specialist_ai_verification",
    "adversarial_publication_ai_verification",
    "static_verification",
    "build_verification",
    "visual_verification",
)


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def duplicate_rejecting_object(
    pairs: list[tuple[str, object]],
) -> dict[str, object]:
    result: dict[str, object] = {}
    for key, value in pairs:
        if key in result:
            raise DuplicateJsonFieldError(f"duplicate JSON field {key!r}")
        result[key] = value
    return result


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require_exact_fields(
    value: object, expected: set[str], location: str
) -> dict[str, object]:
    if not isinstance(value, dict):
        raise ValueError(f"{location}: expected object")
    actual = set(value)
    missing = sorted(expected - actual)
    extra = sorted(actual - expected)
    if missing or extra:
        details: list[str] = []
        if missing:
            details.append(f"missing {missing}")
        if extra:
            details.append(f"unexpected {extra}")
        raise ValueError(f"{location}: exact field set required ({'; '.join(details)})")
    return value


def require_nonempty_string(value: object, location: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{location}: expected nonempty string")
    if value != value.strip():
        raise ValueError(f"{location}: leading or trailing whitespace is forbidden")
    return value


def require_sha256(value: object, location: str) -> str:
    if not isinstance(value, str) or SHA256_RE.fullmatch(value) is None:
        raise ValueError(f"{location}: expected lowercase SHA-256")
    return value


def repo_file(
    root: Path, raw_path: object, location: str, *, prefix: str | None = None
) -> tuple[str, Path]:
    value = require_nonempty_string(raw_path, location)
    if "\\" in value:
        raise ValueError(f"{location}: use repository-relative POSIX path syntax")
    pure = PurePosixPath(value)
    if pure.is_absolute() or any(part in ("", ".", "..") for part in pure.parts):
        raise ValueError(f"{location}: path must remain inside the repository")
    if pure.parts and re.fullmatch(r"[A-Za-z]:", pure.parts[0]) is not None:
        raise ValueError(f"{location}: drive-qualified paths are forbidden")
    if value != pure.as_posix():
        raise ValueError(f"{location}: path must use canonical POSIX syntax")
    if prefix is not None and not value.startswith(prefix):
        raise ValueError(f"{location}: path must start with {prefix!r}")
    resolved_root = root.resolve()
    resolved = (resolved_root / Path(*pure.parts)).resolve()
    try:
        resolved.relative_to(resolved_root)
    except ValueError as exc:
        raise ValueError(f"{location}: path escapes the repository") from exc
    if not resolved.is_file():
        raise ValueError(f"{location}: file does not exist: {value}")
    return value, resolved


def validate_destination_path(
    value: str, location: str, *, allow_part_driver: bool = False
) -> tuple[str, str | None]:
    """Admit maintained content files, never lookup surfaces or drivers."""

    if value.startswith("handbook/generated/") or value.startswith(
        "handbook/registry/"
    ):
        raise ValueError(
            f"{location}: generated and registry lookup surfaces are forbidden"
        )
    if value in FORBIDDEN_LOOKUP_DESTINATIONS:
        raise ValueError(f"{location}: lookup-only destination is forbidden")

    part_match = PART_CONTENT_DESTINATION_RE.fullmatch(value)
    if part_match is not None:
        return "part", f"p{part_match.group('number')}"
    part_driver_match = PART_DRIVER_DESTINATION_RE.fullmatch(value)
    if part_driver_match is not None:
        if allow_part_driver:
            return "restoration integration", f"p{part_driver_match.group('number')}"
        raise ValueError(
            f"{location}: a part driver is permitted only as an exact open "
            "restoration integration destination"
        )
    annex_match = ANNEX_CONTENT_DESTINATION_RE.fullmatch(value)
    if annex_match is not None:
        return "annex", f"p{annex_match.group('number')}"
    if RESTORATION_DESTINATION_RE.fullmatch(value) is not None:
        return "restoration", None
    if value == FRONTMATTER_DESTINATION:
        return "frontmatter", None
    raise ValueError(
        f"{location}: destination must be a nested .tex content file under "
        "handbook/parts/pNN/, handbook/annex/pNN/, or handbook/restoration/, "
        "or the substantive handbook/frontmatter.tex file; a part driver is "
        "eligible only for an open restoration integration record, and other "
        "drivers and lookup-only files are forbidden"
    )


def validate_unit_label(
    label: object,
    destination_kind: str,
    destination_part: str | None,
    location: str,
) -> str:
    """Apply the handbook taxonomy and destination ownership convention."""

    if not isinstance(label, str) or LABEL_RE.fullmatch(label) is None:
        raise ValueError(f"{location}: malformed stable label")
    if UNIT_LABEL_RE.fullmatch(label) is None and not (
        destination_kind == "restoration" and label.startswith("ex:")
    ):
        raise ValueError(
            f"{location}: part, sheet, and rule labels name structural or lookup "
            "surfaces, not content units"
        )
    prefix, identifier = label.split(":", 1)
    if destination_kind == "part":
        if prefix not in {"sec", "entry", "def", "thm", "tab", "fig"}:
            raise ValueError(
                f"{location}: part content requires a substantive part-owned label"
            )
        if destination_part is None or not identifier.startswith(
            f"{destination_part}-"
        ):
            raise ValueError(
                f"{location}: label id must begin {destination_part}- to match "
                "its part-owned destination"
            )
    elif destination_kind == "annex":
        if prefix != "annex":
            raise ValueError(f"{location}: annex content requires an annex: label")
        if destination_part is None or not identifier.startswith(
            f"{destination_part}-"
        ):
            raise ValueError(
                f"{location}: label id must begin {destination_part}- to match "
                "its annex destination"
            )
    return label


def tex_without_comments(text: str) -> str:
    """Remove unescaped TeX comments for exact active-label counting."""

    output: list[str] = []
    for line in text.splitlines(keepends=True):
        cut = len(line)
        for index, char in enumerate(line):
            if char != "%":
                continue
            backslashes = 0
            cursor = index - 1
            while cursor >= 0 and line[cursor] == "\\":
                backslashes += 1
                cursor -= 1
            if backslashes % 2 == 0:
                cut = index
                break
        output.append(line[:cut])
        if cut != len(line) and line.endswith(("\n", "\r")):
            output.append("\n")
    return "".join(output)


def active_label_occurrences(text: str, label: str) -> int:
    """Count active labels in plain commands and the typed handbook grammar."""

    count = 0
    active_text = tex_without_comments(text)
    escaped_label = re.escape(label)
    environments = "|".join(re.escape(name) for name in LABEL_OWNER_ENVIRONMENTS)
    patterns = (
        re.compile(r"\\label\s*\{\s*" + escaped_label + r"\s*\}"),
        re.compile(
            r"\\begin\s*\{\s*(?:"
            + environments
            + r")\s*\}\s*\{\s*"
            + escaped_label
            + r"\s*\}"
        ),
        re.compile(
            r"\\(?:calculussheet|hbrule)\s*\{\s*"
            + escaped_label
            + r"\s*\}"
        ),
    )
    for pattern in patterns:
        for match in pattern.finditer(active_text):
            preceding_backslashes = 0
            cursor = match.start() - 1
            while cursor >= 0 and active_text[cursor] == "\\":
                preceding_backslashes += 1
                cursor -= 1
            if preceding_backslashes % 2 == 0:
                count += 1
    return count


def normalized_static_tex_input(raw: str, location: str) -> str | None:
    """Normalize a literal TeX input; return None for a dynamic expression."""

    value = raw.strip()
    while value.startswith("./"):
        value = value[2:]
    if not value or any(marker in value for marker in ("\\", "#", "$", "{")):
        return None
    pure = PurePosixPath(value)
    if pure.is_absolute() or any(part in ("", ".", "..") for part in pure.parts):
        raise ValueError(f"{location}: static input escapes the handbook")
    if pure.parts and re.fullmatch(r"[A-Za-z]:", pure.parts[0]) is not None:
        raise ValueError(f"{location}: drive-qualified static input is forbidden")
    if pure.suffix == "":
        pure = pure.with_suffix(".tex")
    return pure.as_posix()


def recursive_static_input_counts(repository_root: Path) -> dict[str, int]:
    """Count literal input executions reachable from handbook/main.tex."""

    repository_root = repository_root.resolve()
    handbook_root = (repository_root / "handbook").resolve()
    counts: dict[str, int] = {}

    def visit(relative: str, active: tuple[str, ...]) -> None:
        if relative in active:
            cycle = " -> ".join((*active, relative))
            raise ValueError(f"handbook static input cycle prevents proof: {cycle}")
        lexical = repository_root / Path(*f"handbook/{relative}".split("/"))
        resolved = lexical.resolve()
        try:
            resolved_relative = resolved.relative_to(repository_root).as_posix()
        except ValueError as exc:
            raise ValueError(
                f"handbook/{relative}: static input escapes the repository"
            ) from exc
        if resolved_relative != f"handbook/{relative}":
            raise ValueError(
                f"handbook/{relative}: symbolic-link or junction indirection is forbidden"
            )
        try:
            resolved.relative_to(handbook_root)
        except ValueError as exc:
            raise ValueError(
                f"handbook/{relative}: static input escapes the handbook"
            ) from exc
        if not resolved.is_file():
            raise ValueError(
                f"handbook/{relative}: reachable static input does not exist"
            )
        try:
            text = resolved.read_text(encoding="utf-8", errors="strict")
        except (OSError, UnicodeError) as exc:
            raise ValueError(
                f"handbook/{relative}: cannot read reachable static input: {exc}"
            ) from exc
        active_text = tex_without_comments(text)
        active_text = re.sub(
            r"\\begin\{(lstlisting|verbatim)\}.*?\\end\{\1\}",
            lambda match: "\n" * match.group(0).count("\n"),
            active_text,
            flags=re.DOTALL,
        )
        active_text = re.sub(
            r"\\verb\*?(?P<delimiter>[^A-Za-z\s]).*?(?P=delimiter)",
            "",
            active_text,
        )
        next_active = (*active, relative)
        for match_index, match in enumerate(
            STATIC_TEX_INPUT_RE.finditer(active_text), start=1
        ):
            preceding_backslashes = 0
            cursor = match.start() - 1
            while cursor >= 0 and active_text[cursor] == "\\":
                preceding_backslashes += 1
                cursor -= 1
            if preceding_backslashes % 2:
                continue
            raw_target = match.group(1) or match.group(2)
            target = normalized_static_tex_input(
                raw_target, f"handbook/{relative} input {match_index}"
            )
            if target is None:
                continue
            counts[target] = counts.get(target, 0) + 1
            visit(target, next_active)

    visit("main.tex", ())
    return counts


def validate_restoration_wrapper(
    repository_root: Path,
    provenance_id: str,
    restoration_record: dict[str, object],
) -> str:
    """Check the exact wrapper-to-artifact relationship and return its path."""

    wrapper_value = f"handbook/restoration/scope-{provenance_id}.tex"
    _, wrapper_file = repo_file(
        repository_root,
        wrapper_value,
        f"restoration wrapper for {provenance_id}",
        prefix="handbook/restoration/",
    )
    if wrapper_file.relative_to(repository_root.resolve()).as_posix() != wrapper_value:
        raise ValueError(
            f"restoration wrapper for {provenance_id}: symbolic-link or junction "
            "indirection is forbidden"
        )
    wrapper_text = tex_without_comments(
        wrapper_file.read_text(encoding="utf-8", errors="strict")
    )
    wrapper_match = re.fullmatch(
        r"\s*\\begin\{inheritedrestorationscope\}\s*\{"
        + re.escape(provenance_id)
        + r"\}\s*\\input\s*\{([^{}]+)\}\s*"
        r"\\end\{inheritedrestorationscope\}\s*",
        wrapper_text,
    )
    if wrapper_match is None:
        raise ValueError(
            f"restoration wrapper for {provenance_id}: expected exactly one "
            "governed artifact input"
        )
    artifact = restoration_record["restoration_artifact"]
    if not isinstance(artifact, dict) or not isinstance(artifact.get("path"), str):
        raise ValueError(
            f"restoration wrapper for {provenance_id}: validated record has no "
            "artifact path"
        )
    recorded_artifact = artifact["path"]
    if not recorded_artifact.startswith("handbook/"):
        raise ValueError(
            f"restoration wrapper for {provenance_id}: artifact path is not under "
            "handbook/"
        )
    expected_input = normalized_static_tex_input(
        recorded_artifact.removeprefix("handbook/"),
        f"restoration record {provenance_id} artifact path",
    )
    wrapper_input = normalized_static_tex_input(
        wrapper_match.group(1), f"restoration wrapper for {provenance_id} input"
    )
    if wrapper_input != expected_input:
        raise ValueError(
            f"restoration wrapper for {provenance_id}: artifact input does not "
            "match the validated restoration record"
        )
    return wrapper_value.removeprefix("handbook/")


def validate_restoration_record_link(
    record: dict[str, object],
    base: dict[str, str],
    ordinal: int,
    location: str,
    repository_root: Path,
    static_input_counts: dict[str, int],
) -> tuple[Path, dict[str, object]]:
    """Require one exact validated restoration record for a reviewed unit."""

    provenance_id = require_nonempty_string(
        record["restoration_provenance_id"],
        f"{location}.restoration_provenance_id",
    )
    if RESTORATION_PROVENANCE_ID_RE.fullmatch(provenance_id) is None:
        raise ValueError(
            f"{location}.restoration_provenance_id: malformed provenance id"
        )
    record_value, record_file = repo_file(
        repository_root,
        record["restoration_record_path"],
        f"{location}.restoration_record_path",
        prefix="spec/provenance/",
    )
    path_match = RESTORATION_RECORD_PATH_RE.fullmatch(record_value)
    if path_match is None:
        raise ValueError(
            f"{location}.restoration_record_path: expected a canonical inherited "
            "restoration record path directly under spec/provenance/"
        )
    if path_match.group("provenance_id") != provenance_id:
        raise ValueError(
            f"{location}.restoration_provenance_id: does not match the record path"
        )
    if record_file.relative_to(repository_root.resolve()).as_posix() != record_value:
        raise ValueError(
            f"{location}.restoration_record_path: symbolic-link or junction "
            "indirection is forbidden"
        )
    expected_hash = require_sha256(
        record["restoration_record_sha256"],
        f"{location}.restoration_record_sha256",
    )
    if sha256_file(record_file) != expected_hash:
        raise ValueError(f"{location}: restoration record SHA-256 drift")

    try:
        restoration_record = inherited_restoration.load_json(record_file)
        verified_id = inherited_restoration.validate_record(
            restoration_record, record_file, repository_root.resolve()
        )
    except Exception as exc:
        raise ValueError(
            f"{location}: inherited restoration validation failed: {exc}"
        ) from exc
    if verified_id != provenance_id:
        raise ValueError(
            f"{location}.restoration_provenance_id: validated record id mismatch"
        )
    corrected = restoration_record["schema_version"] == 4
    if corrected:
        expected_identity = (
            f"{provenance_id}:{restoration_record['reader_correction']['correction_id']}:unit-{ordinal}"
        )
        if record["presentation_identity_value"] != expected_identity:
            raise ValueError(f"{location}: corrected presentation identity must be {expected_identity!r}")
        artifact = restoration_record["restoration_artifact"]
        if (record["handbook_destination"] != artifact["path"]
                or record["handbook_destination_sha256"] != artifact["sha256"]):
            raise ValueError(f"{location}: corrected destination must match the exact version-4 artifact")
        if static_input_counts.get(artifact["path"].removeprefix("handbook/"), 0) != 1:
            raise ValueError(f"{location}: corrected reader artifact must be reachable exactly once")
        if (not isinstance(record["provenance_disposition"], str)
                or record["provenance_disposition"] not in {OPEN_DISPOSITION, CORRECTED_DISPOSITION}):
            raise ValueError(f"{location}: corrected reader cannot claim full transcription")
        if (not isinstance(record["audit_result"], str)
                or record["audit_result"] not in {PENDING_AUDIT_RESULT, CORRECTED_AUDIT_RESULT}):
            raise ValueError(f"{location}: corrected reader requires a corrected audit result")
        if ((record["provenance_disposition"] == CORRECTED_DISPOSITION)
                != (record["audit_result"] == CORRECTED_AUDIT_RESULT)):
            raise ValueError(f"{location}: full reconstruction must pair with corrected-and-verified")
    elif record["provenance_disposition"] == CORRECTED_DISPOSITION or record["audit_result"] == CORRECTED_AUDIT_RESULT:
        raise ValueError(f"{location}: corrected admission requires a validated version-4 record")
    elif restoration_record["disposition"] != PASSING_DISPOSITION:
        raise ValueError(
            f"{location}.restoration_record_path: disposition must be "
            f"{PASSING_DISPOSITION!r}"
        )

    evidence = restoration_record["source_unit_evidence"]
    raw_ordinals = evidence["unit_ordinals"]
    if ordinal not in raw_ordinals:
        raise ValueError(
            f"{location}.restoration_record_path: source_unit_evidence does not "
            f"contain reviewed unit ordinal {ordinal}"
        )
    locator = restoration_record["source_locator"]
    unit_start = int(base["source_start"])
    unit_end = int(base["source_end"])
    if not (
        int(locator["start_line"]) <= unit_start
        and unit_end <= int(locator["end_line"])
    ):
        raise ValueError(
            f"{location}.restoration_record_path: source locator does not contain "
            f"reviewed unit range {unit_start}--{unit_end}"
        )

    _, inventory_file = repo_file(
        repository_root,
        evidence["inventory"],
        f"{location}.restoration source-unit inventory",
    )
    inventory_rows = read_rows(inventory_file)
    matching_rows = [
        item for item in inventory_rows if item.get("ordinal") == str(ordinal)
    ]
    if len(matching_rows) != 1:
        raise ValueError(
            f"{location}.restoration_record_path: source_unit_evidence does not "
            f"resolve unit ordinal {ordinal} exactly once"
        )
    inventory_unit = matching_rows[0]
    expected_inventory_identity = {
        "kind": base["unit_kind"],
        "title": base["unit_title"],
        "label": base["unit_source_label"],
        "start_line": base["source_start"],
        "end_line": base["source_end"],
        "sha256": base["source_sha256"],
    }
    for field, expected in expected_inventory_identity.items():
        if inventory_unit.get(field) != expected:
            raise ValueError(
                f"{location}.restoration_record_path: source_unit_evidence has "
                f"the wrong reviewed-unit {field}"
            )

    wrapper = validate_restoration_wrapper(
        repository_root, provenance_id, restoration_record
    )
    wrapper_count = static_input_counts.get(wrapper, 0)
    if wrapper_count != 1:
        raise ValueError(
            f"{location}.restoration_record_path: governed wrapper {wrapper!r} "
            f"is reachable {wrapper_count} times from handbook/main.tex; expected "
            "exactly once"
        )
    return record_file, restoration_record


def exact_string_list(
    value: object, expected: tuple[str, ...], location: str
) -> list[str]:
    if not isinstance(value, list) or value != list(expected):
        raise ValueError(f"{location}: expected exact ordered list {list(expected)!r}")
    return list(expected)


def exact_result_map(
    value: object, expected: tuple[str, ...], location: str
) -> dict[str, str]:
    raw = require_exact_fields(value, set(expected), location)
    result: dict[str, str] = {}
    for key in expected:
        item = raw[key]
        if not isinstance(item, str) or item not in RESULT_VALUES:
            raise ValueError(
                f"{location}.{key}: expected one of {sorted(RESULT_VALUES)}"
            )
        result[key] = item
    return result


def apply_reviewed_records(
    rows: list[dict[str, str]],
    reviewed_records_path: Path | None,
    source_hash: str,
    repository_root: Path,
) -> list[dict[str, str]]:
    """Validate reviewer-supplied records, then overlay only governed fields."""

    if reviewed_records_path is None:
        return rows
    if not reviewed_records_path.is_file():
        raise ValueError(f"reviewed-record input does not exist: {reviewed_records_path}")
    try:
        document = json.loads(
            reviewed_records_path.read_text(encoding="utf-8"),
            object_pairs_hook=duplicate_rejecting_object,
        )
    except (UnicodeDecodeError, json.JSONDecodeError, DuplicateJsonFieldError) as exc:
        raise ValueError(f"invalid reviewed-record JSON: {exc}") from exc

    document = require_exact_fields(
        document,
        {"schema_version", "authority_path", "authority_sha256", "records"},
        "reviewed-record document",
    )
    if (
        isinstance(document["schema_version"], bool)
        or not isinstance(document["schema_version"], int)
        or document["schema_version"] != REVIEW_SCHEMA_VERSION
    ):
        raise ValueError(
            "reviewed-record document: schema_version must be "
            f"{REVIEW_SCHEMA_VERSION}"
        )
    if document["authority_path"] != AUTHORITY_PATH:
        raise ValueError(
            f"reviewed-record document: authority_path must be {AUTHORITY_PATH!r}"
        )
    document_authority_hash = require_sha256(
        document["authority_sha256"], "reviewed-record document.authority_sha256"
    )
    if document_authority_hash != source_hash:
        raise ValueError("reviewed-record document: authority SHA-256 drift")
    _, authority_file = repo_file(
        repository_root, document["authority_path"], "reviewed-record authority_path"
    )
    if sha256_file(authority_file) != source_hash:
        raise ValueError("reviewed-record document: live authority hash mismatch")
    records = document["records"]
    if not isinstance(records, list):
        raise ValueError("reviewed-record document.records: expected array")
    if records and source_hash != AUTHORITY_SHA256:
        raise ValueError(
            "reviewed-record document: live authority is not the exact frozen authority"
        )
    static_input_counts = (
        recursive_static_input_counts(repository_root) if records else {}
    )

    by_ordinal = {int(row["unit_ordinal"]): row for row in rows}
    seen_ordinals: set[int] = set()
    claimed_labels: dict[str, int] = {}
    overlays: dict[int, dict[str, str]] = {}
    variant_targets_by_ordinal: dict[int, set[int]] = {}
    presentation_identity_by_ordinal: dict[int, str] = {}

    for index, untyped_record in enumerate(records):
        location = f"reviewed-record document.records[{index}]"
        record = require_exact_fields(untyped_record, REVIEW_RECORD_FIELDS, location)
        ordinal = record["unit_ordinal"]
        if isinstance(ordinal, bool) or not isinstance(ordinal, int):
            raise ValueError(f"{location}.unit_ordinal: expected integer")
        if ordinal in seen_ordinals:
            raise ValueError(f"{location}: duplicate unit ordinal {ordinal}")
        seen_ordinals.add(ordinal)
        if ordinal not in by_ordinal:
            raise ValueError(f"{location}: unknown unit ordinal {ordinal}")
        base = by_ordinal[ordinal]

        exact_identity = {
            "unit_kind": base["unit_kind"],
            "unit_title": base["unit_title"],
            "unit_source_label": base["unit_source_label"],
            "source_start": int(base["source_start"]),
            "source_end": int(base["source_end"]),
            "source_sha256": base["source_sha256"],
            "authority_path": AUTHORITY_PATH,
            "authority_sha256": source_hash,
        }
        for field in ("source_start", "source_end"):
            if isinstance(record[field], bool) or not isinstance(record[field], int):
                raise ValueError(f"{location}.{field}: expected integer")
        for field, expected in exact_identity.items():
            if record[field] != expected:
                raise ValueError(
                    f"{location}.{field}: stale or mismatched unit identity; "
                    f"expected {expected!r}"
                )

        restoration_record_file, restoration_record = validate_restoration_record_link(
            record,
            base,
            ordinal,
            location,
            repository_root,
            static_input_counts,
        )

        if record["authority_edition_status"] != "identified":
            raise ValueError(f"{location}.authority_edition_status: must be 'identified'")
        if record["authority_edition_value"] != AUTHORITY_EDITION:
            raise ValueError(
                f"{location}.authority_edition_value: expected exact frozen edition "
                f"{AUTHORITY_EDITION!r}"
            )
        authority_edition = AUTHORITY_EDITION
        if record["presentation_identity_status"] != "identified":
            raise ValueError(
                f"{location}.presentation_identity_status: must be 'identified'"
            )
        presentation_identity = require_nonempty_string(
            record["presentation_identity_value"],
            f"{location}.presentation_identity_value",
        )
        presentation_description = require_nonempty_string(
            record["presentation_identity_description"],
            f"{location}.presentation_identity_description",
        )

        disposition = record["provenance_disposition"]
        if not isinstance(disposition, str) or disposition not in PERMITTED_DISPOSITIONS:
            raise ValueError(
                f"{location}.provenance_disposition: expected one of "
                f"{sorted(PERMITTED_DISPOSITIONS)}"
            )
        if record["handbook_destination_status"] != "identified":
            raise ValueError(
                f"{location}.handbook_destination_status: must be 'identified'"
            )
        destination_value, destination_file = repo_file(
            repository_root,
            record["handbook_destination"],
            f"{location}.handbook_destination",
            prefix="handbook/",
        )
        destination_kind, destination_part = validate_destination_path(
            destination_value,
            f"{location}.handbook_destination",
            allow_part_driver=disposition == OPEN_DISPOSITION,
        )
        resolved_destination_value = destination_file.relative_to(
            repository_root.resolve()
        ).as_posix()
        if resolved_destination_value != destination_value:
            raise ValueError(
                f"{location}.handbook_destination: symbolic-link or junction "
                "indirection is forbidden"
            )
        destination_hash = require_sha256(
            record["handbook_destination_sha256"],
            f"{location}.handbook_destination_sha256",
        )
        if sha256_file(destination_file) != destination_hash:
            raise ValueError(f"{location}: handbook destination SHA-256 drift")

        labels = record["stable_labels"]
        if not isinstance(labels, list):
            raise ValueError(f"{location}.stable_labels: expected array")
        if disposition in TERMINAL_DISPOSITIONS and not labels:
            raise ValueError(
                f"{location}.stable_labels: {disposition} requires at "
                "least one stable label"
            )
        labels = [
            validate_unit_label(
                label,
                destination_kind,
                destination_part,
                f"{location}.stable_labels[{label_index}]",
            )
            for label_index, label in enumerate(labels)
        ]
        if len(set(labels)) != len(labels):
            raise ValueError(f"{location}.stable_labels: duplicate label")
        destination_text = destination_file.read_text(
            encoding="utf-8", errors="strict"
        )
        for label in labels:
            occurrences = active_label_occurrences(destination_text, label)
            if occurrences != 1:
                raise ValueError(
                    f"{location}.stable_labels: {label!r} occurs {occurrences} "
                    "times in the exact destination"
                )
            if label in claimed_labels:
                raise ValueError(
                    f"{location}.stable_labels: {label!r} already closes unit "
                    f"{claimed_labels[label]}"
                )
            claimed_labels[label] = ordinal

        audit_result = record["audit_result"]
        if not isinstance(audit_result, str) or audit_result not in AUDIT_RESULTS:
            raise ValueError(
                f"{location}.audit_result: expected one of {list(AUDIT_RESULTS)}"
            )
        layout_changes = record["layout_changes"]
        if not isinstance(layout_changes, list) or any(
            not isinstance(item, str) or item not in LAYOUT_CHANGES
            for item in layout_changes
        ):
            raise ValueError(
                f"{location}.layout_changes: expected only {list(LAYOUT_CHANGES)}"
            )
        if len(set(layout_changes)) != len(layout_changes):
            raise ValueError(f"{location}.layout_changes: duplicate value")
        if audit_result == PENDING_AUDIT_RESULT:
            if disposition != OPEN_DISPOSITION:
                raise ValueError(
                    f"{location}.audit_result: {PENDING_AUDIT_RESULT!r} is "
                    "permitted only for an open/missing record"
                )
            if layout_changes:
                raise ValueError(
                    f"{location}.layout_changes: {PENDING_AUDIT_RESULT!r} "
                    "requires an empty list"
                )
            exact_string_list(
                record["defect_exclusions"],
                (),
                f"{location}.defect_exclusions",
            )
        elif audit_result == "full-and-accurate" and layout_changes:
            raise ValueError(
                f"{location}.layout_changes: full-and-accurate requires an empty list"
            )
        elif audit_result == "layout-only relocation" and not layout_changes:
            raise ValueError(
                f"{location}.layout_changes: layout-only relocation requires at "
                "least one permitted layout change"
            )
        if audit_result in PASSING_AUDIT_RESULTS:
            exact_string_list(
                record["defect_exclusions"],
                CORRECTED_DEFECT_EXCLUSIONS if audit_result == CORRECTED_AUDIT_RESULT else DEFECT_EXCLUSIONS,
                f"{location}.defect_exclusions",
            )

        variant_links = record["variant_links"]
        if not isinstance(variant_links, list):
            raise ValueError(f"{location}.variant_links: expected array")
        variant_targets: set[int] = set()
        for link_index, untyped_link in enumerate(variant_links):
            link_location = f"{location}.variant_links[{link_index}]"
            link = require_exact_fields(
                untyped_link, VARIANT_LINK_FIELDS, link_location
            )
            target_ordinal = link["unit_ordinal"]
            if isinstance(target_ordinal, bool) or not isinstance(target_ordinal, int):
                raise ValueError(f"{link_location}.unit_ordinal: expected integer")
            if target_ordinal == ordinal:
                raise ValueError(f"{link_location}: a unit cannot link itself as a variant")
            if target_ordinal in variant_targets:
                raise ValueError(
                    f"{link_location}: duplicate variant unit ordinal {target_ordinal}"
                )
            if target_ordinal not in by_ordinal:
                raise ValueError(
                    f"{link_location}: unknown variant unit ordinal {target_ordinal}"
                )
            variant_targets.add(target_ordinal)
            target = by_ordinal[target_ordinal]
            exact_target_identity = {
                "unit_source_label": target["unit_source_label"],
                "source_start": int(target["source_start"]),
                "source_end": int(target["source_end"]),
                "source_sha256": target["source_sha256"],
            }
            for field in ("source_start", "source_end"):
                if isinstance(link[field], bool) or not isinstance(link[field], int):
                    raise ValueError(f"{link_location}.{field}: expected integer")
            for field, expected in exact_target_identity.items():
                if link[field] != expected:
                    raise ValueError(
                        f"{link_location}.{field}: stale or mismatched variant "
                        f"identity; expected {expected!r}"
                    )
            require_nonempty_string(
                link["relationship"], f"{link_location}.relationship"
            )
        variant_targets_by_ordinal[ordinal] = variant_targets
        presentation_identity_by_ordinal[ordinal] = presentation_identity

        completeness = exact_result_map(
            record["completeness"], COMPLETENESS_FIELDS, f"{location}.completeness"
        )
        verification = exact_result_map(
            record["verification"], VERIFICATION_FIELDS, f"{location}.verification"
        )

        evidence = record["verification_evidence"]
        if not isinstance(evidence, list) or len(evidence) > len(VERIFICATION_FIELDS):
            raise ValueError(
                f"{location}.verification_evidence: expected at most "
                f"{len(VERIFICATION_FIELDS)} records"
            )
        evidence_kinds: set[str] = set()
        evidence_files: list[Path] = []
        producer_identities: set[str] = set()
        forbidden_files = {
            authority_file.resolve(),
            destination_file.resolve(),
            reviewed_records_path.resolve(),
        }
        for evidence_index, untyped_evidence in enumerate(evidence):
            evidence_location = (
                f"{location}.verification_evidence[{evidence_index}]"
            )
            if not isinstance(untyped_evidence, dict):
                raise ValueError(f"{evidence_location}: expected object")
            kind = untyped_evidence.get("category")
            if not isinstance(kind, str) or kind not in VERIFICATION_FIELDS:
                raise ValueError(
                    f"{evidence_location}.category: expected one of "
                    f"{list(VERIFICATION_FIELDS)}"
                )
            is_passing_ai_review = (
                kind in AI_REVIEW_FIELDS
                and untyped_evidence.get("recorded_result") == "pass"
            )
            corrected = restoration_record["schema_version"] == 4
            item = require_exact_fields(
                untyped_evidence,
                (AI_EVIDENCE_FIELDS if is_passing_ai_review else EVIDENCE_FIELDS)
                | ({"correction_snapshot"} if corrected else set()),
                evidence_location,
            )
            if corrected:
                snapshot = require_exact_fields(
                    item["correction_snapshot"], set(CORRECTION_SNAPSHOT_FIELDS),
                    f"{evidence_location}.correction_snapshot",
                )
                if any(type(snapshot[field]) is not type(record[field])
                       or snapshot[field] != record[field] for field in CORRECTION_SNAPSHOT_FIELDS):
                    raise ValueError(f"{evidence_location}: correction snapshot differs from the reviewed unit/destination")
            if kind in evidence_kinds:
                raise ValueError(
                    f"{evidence_location}: duplicate evidence category {kind}"
                )
            evidence_kinds.add(kind)
            if item["recorded_result"] != verification[kind]:
                raise ValueError(
                    f"{evidence_location}.recorded_result: does not match "
                    f"verification.{kind}"
                )
            evidence_path, evidence_file = repo_file(
                repository_root,
                item["artifact_path"],
                f"{evidence_location}.artifact_path",
            )
            if any(evidence_file.samefile(existing) for existing in evidence_files):
                raise ValueError(
                    f"{evidence_location}.artifact_path: verification dimensions "
                    "must use separate evidence files"
                )
            evidence_files.append(evidence_file)
            if any(evidence_file.samefile(forbidden) for forbidden in forbidden_files):
                raise ValueError(
                    f"{evidence_location}.artifact_path: authority, destination, "
                    "and review input cannot serve as their own evidence artifact"
                )
            if evidence_file.samefile(restoration_record_file) and not (
                disposition == OPEN_DISPOSITION and kind == "static"
            ):
                raise ValueError(
                    f"{evidence_location}.artifact_path: the linked restoration "
                    "record may support only static verification on an open record"
                )
            evidence_hash = require_sha256(
                item["sha256"], f"{evidence_location}.sha256"
            )
            if sha256_file(evidence_file) != evidence_hash:
                raise ValueError(f"{evidence_location}: evidence SHA-256 drift")
            producer_identity = require_nonempty_string(
                item["producer_identity"],
                f"{evidence_location}.producer_identity",
            )
            normalized_identity = unicodedata.normalize(
                "NFKC", producer_identity
            ).casefold()
            normalized_identity = " ".join(normalized_identity.split())
            if normalized_identity in producer_identities:
                raise ValueError(
                    f"{evidence_location}.producer_identity: each verification "
                    "category requires a distinct recorded producer identity"
                )
            producer_identities.add(normalized_identity)
            require_nonempty_string(
                item["recorded_scope"], f"{evidence_location}.recorded_scope"
            )
            if is_passing_ai_review:
                require_nonempty_string(item["model"], f"{evidence_location}.model")
                require_nonempty_string(
                    item["model_version"], f"{evidence_location}.model_version"
                )
                require_nonempty_string(
                    item["instructions"], f"{evidence_location}.instructions"
                )
                if item["other_review_outputs_consulted"] is not False:
                    raise ValueError(
                        f"{evidence_location}.other_review_outputs_consulted: "
                        "independent AI review must record false"
                    )
                findings = item["findings"]
                if not isinstance(findings, list) or not findings:
                    raise ValueError(
                        f"{evidence_location}.findings: expected a nonempty list"
                    )
                for finding_index, finding in enumerate(findings):
                    require_nonempty_string(
                        finding, f"{evidence_location}.findings[{finding_index}]"
                    )
                consulted = item["consulted_authorities"]
                if not isinstance(consulted, list) or not consulted:
                    raise ValueError(
                        f"{evidence_location}.consulted_authorities: expected a "
                        "nonempty list"
                    )
                seen_consulted: set[tuple[str, str]] = set()
                for authority_index, untyped_authority in enumerate(consulted):
                    authority_location = (
                        f"{evidence_location}.consulted_authorities[{authority_index}]"
                    )
                    authority = require_exact_fields(
                        untyped_authority,
                        CONSULTED_AUTHORITY_FIELDS,
                        authority_location,
                    )
                    authority_path, authority_file = repo_file(
                        repository_root,
                        authority["path"],
                        f"{authority_location}.path",
                    )
                    authority_locator = require_nonempty_string(
                        authority["locator"], f"{authority_location}.locator"
                    )
                    identity = (authority_path, authority_locator)
                    if identity in seen_consulted:
                        raise ValueError(
                            f"{authority_location}: duplicate consulted authority"
                        )
                    seen_consulted.add(identity)
                    authority_hash = require_sha256(
                        authority["sha256"], f"{authority_location}.sha256"
                    )
                    if sha256_file(authority_file) != authority_hash:
                        raise ValueError(f"{authority_location}: authority SHA-256 drift")
        missing_recorded_evidence = {
            key
            for key, value in verification.items()
            if value != "pending" and key not in evidence_kinds
        }
        if missing_recorded_evidence:
            raise ValueError(
                f"{location}.verification_evidence: missing evidence for "
                f"non-pending categories {sorted(missing_recorded_evidence)}"
            )

        all_pass = all(value == "pass" for value in completeness.values()) and all(
            value == "pass" for value in verification.values()
        )
        if audit_result in PASSING_AUDIT_RESULTS and not all_pass:
            raise ValueError(
                f"{location}.audit_result: passing audit result requires all "
                "completeness and verification dimensions to pass"
            )
        if disposition in TERMINAL_DISPOSITIONS and not all_pass:
            raise ValueError(
                f"{location}.provenance_disposition: {disposition} requires "
                "all completeness and verification dimensions to pass"
            )
        if disposition in TERMINAL_DISPOSITIONS and evidence_kinds != set(
            VERIFICATION_FIELDS
        ):
            raise ValueError(
                f"{location}.verification_evidence: {disposition} requires "
                "all verification categories"
            )

        overlay = {
            "restoration_provenance_id": str(record["restoration_provenance_id"]),
            "restoration_record_path": str(record["restoration_record_path"]),
            "restoration_record_sha256": str(record["restoration_record_sha256"]),
            "authority_edition_status": "identified",
            "authority_edition_value": authority_edition,
            "presentation_identity_status": "identified",
            "presentation_identity_value": presentation_identity,
            "presentation_identity_description": presentation_description,
            "provenance_disposition": str(disposition),
            "handbook_destination_status": "identified",
            "handbook_destination": destination_value,
            "stable_labels": json.dumps(labels, ensure_ascii=False),
            "audit_result": str(audit_result),
        }
        overlay.update(
            {f"{key}_completeness": value for key, value in completeness.items()}
        )
        overlay.update(
            {VERIFICATION_OUTPUT_FIELDS[key]: value for key, value in verification.items()}
        )
        overlays[ordinal] = overlay

    for ordinal, targets in variant_targets_by_ordinal.items():
        for target in targets:
            if target not in seen_ordinals:
                raise ValueError(
                    f"reviewed unit {ordinal}: linked variant unit {target} is not "
                    "separately recorded in this input"
                )
            if ordinal not in variant_targets_by_ordinal.get(target, set()):
                raise ValueError(
                    f"reviewed unit {ordinal}: linked variant unit {target} does not "
                    "record the reciprocal link"
                )
            if (
                presentation_identity_by_ordinal[ordinal]
                == presentation_identity_by_ordinal[target]
            ):
                raise ValueError(
                    f"reviewed unit {ordinal}: linked variant unit {target} must have "
                    "a different presentation identity"
                )

    return [dict(row, **overlays.get(int(row["unit_ordinal"]), {})) for row in rows]


def is_terminal_source_unit(row: dict[str, str]) -> bool:
    """Disposition/result only; callers must validate records and all gates."""
    return (
        row.get("provenance_disposition") == PASSING_DISPOSITION
        and row.get("audit_result") in EXACT_AUDIT_RESULTS
    ) or (
        row.get("provenance_disposition") == CORRECTED_DISPOSITION
        and row.get("audit_result") == CORRECTED_AUDIT_RESULT
    )


def validated_reviewed_rows(repository_root: Path) -> list[dict[str, str]]:
    """Revalidate admissions from frozen inventory identities, without CSV trust.

    This is the same record join used by build_rows. It does not generate a
    crosswalk or replace build_rows' complete audit-interval coverage checks.
    """
    source = repository_root / AUTHORITY_PATH
    source_hash = sha256_file(source)
    lines = source.read_bytes().decode("utf-8").splitlines(keepends=True)
    rows: list[dict[str, str]] = []
    seen: set[int] = set()
    for unit in read_rows(repository_root / "spec/source-unit-inventory.csv"):
        ordinal, start, end = int(unit["ordinal"]), int(unit["start_line"]), int(unit["end_line"])
        if ordinal in seen or not (1 <= start <= end <= len(lines)):
            raise ValueError("corrected admission: duplicate ordinal or invalid source range")
        seen.add(ordinal)
        if interval_digest(lines, start, end) != unit["sha256"]:
            raise ValueError(f"corrected admission: source digest mismatch for unit {ordinal}")
        row = {field: "" for field in OUTPUT_FIELDS}
        row.update({
            "unit_ordinal": str(ordinal), "unit_kind": unit["kind"],
            "unit_title": unit["title"], "unit_source_label": unit["label"],
            "source_start": str(start), "source_end": str(end),
            "source_sha256": unit["sha256"], "authority_path": AUTHORITY_PATH,
            "authority_sha256": source_hash, "provenance_disposition": OPEN_DISPOSITION,
            "authority_edition_status": "pending",
            "presentation_identity_status": OPEN_DISPOSITION,
            "handbook_destination_status": OPEN_DISPOSITION,
            "stable_labels": "[]", "audit_result": "pending",
        })
        row.update({f"{field}_completeness": "pending" for field in COMPLETENESS_FIELDS})
        row.update({field: "pending" for field in VERIFICATION_OUTPUT_FIELDS.values()})
        rows.append(row)
    return apply_reviewed_records(
        rows, repository_root / "spec/provenance/reviewed-source-unit-records.json",
        source_hash, repository_root,
    )


def require_corrected_reader_admissions(
    repository_root: Path, provenance_ids: set[str],
    emitted_labels: dict[str, set[str]] | None = None,
    artifact_hashes: dict[str, str] | None = None,
) -> dict[str, dict[str, str]]:
    """Require every unit and emitted label of each corrected reader to be admitted."""
    admitted = {row["unit_ordinal"]: row for row in validated_reviewed_rows(repository_root)}
    for provenance_id in sorted(provenance_ids):
        if RESTORATION_PROVENANCE_ID_RE.fullmatch(provenance_id) is None:
            raise ValueError("corrected admission: malformed provenance ID")
        path = repository_root / f"spec/provenance/{provenance_id}.json"
        record = inherited_restoration.load_json(path)
        inherited_restoration.validate_record(record, path, repository_root)
        if record["schema_version"] != 4:
            raise ValueError(f"{provenance_id}: corrected admission requires version 4")
        if artifact_hashes is not None and artifact_hashes.get(provenance_id) != record["restoration_artifact"]["sha256"]:
            raise ValueError(f"{provenance_id}: collected reader bytes differ from admitted artifact")
        labels: set[str] = set()
        ordinals = record["source_unit_evidence"]["unit_ordinals"]
        if not ordinals:
            raise ValueError(f"{provenance_id}: corrected reader has no reviewed source units")
        for ordinal in ordinals:
            row = admitted.get(str(ordinal), {})
            if (not is_terminal_source_unit(row)
                    or row.get("provenance_disposition") != CORRECTED_DISPOSITION
                    or row.get("restoration_provenance_id") != provenance_id):
                raise ValueError(f"{provenance_id}: corrected reader unit {ordinal} still needs terminal admission")
            labels.update(json.loads(row["stable_labels"]))
        if emitted_labels is not None and not emitted_labels.get(provenance_id, set()).issubset(labels):
            raise ValueError(f"{provenance_id}: emitted correction labels lack exact unit admission")
    return admitted


def interval_digest(lines: list[str], start: int, end: int) -> str:
    return hashlib.sha256("".join(lines[start - 1 : end]).encode("utf-8")).hexdigest()


def build_rows(
    inventory_path: Path,
    audit_map_path: Path,
    source_path: Path,
    reviewed_records_path: Path | None = DEFAULT_REVIEWED_RECORDS,
    repository_root: Path = ROOT,
) -> tuple[list[dict[str, str]], str]:
    source_bytes = source_path.read_bytes()
    source_hash = hashlib.sha256(source_bytes).hexdigest()
    source_lines = source_bytes.decode("utf-8").splitlines(keepends=True)

    if reviewed_records_path is not None and source_hash != AUTHORITY_SHA256:
        raise ValueError(
            "reviewed-record processing requires the exact frozen authority"
        )
    units = read_rows(inventory_path)
    intervals = read_rows(audit_map_path)
    if len(units) != 1055:
        raise ValueError(f"expected 1055 inventory units, found {len(units)}")

    parsed_intervals: list[tuple[int, int, dict[str, str]]] = []
    for row in intervals:
        start = int(row["source_start"])
        end = int(row["source_end"])
        parsed_intervals.append((start, end, row))

    output: list[dict[str, str]] = []
    ordinals: set[int] = set()
    for unit in units:
        ordinal = int(unit["ordinal"])
        if ordinal in ordinals:
            raise ValueError(f"duplicate unit ordinal {ordinal}")
        ordinals.add(ordinal)
        start = int(unit["start_line"])
        end = int(unit["end_line"])
        if not (1 <= start <= end <= len(source_lines)):
            raise ValueError(f"unit {ordinal}: invalid source interval {start}--{end}")
        actual_digest = interval_digest(source_lines, start, end)
        if actual_digest != unit["sha256"]:
            raise ValueError(f"unit {ordinal}: source digest mismatch")

        overlaps = [
            row
            for interval_start, interval_end, row in parsed_intervals
            if interval_start <= end and interval_end >= start
        ]
        coverage = [0] * (end - start + 1)
        for row in overlaps:
            interval_start = int(row["source_start"])
            interval_end = int(row["source_end"])
            for line in range(max(start, interval_start), min(end, interval_end) + 1):
                coverage[line - start] += 1
        if any(count != 1 for count in coverage):
            raise ValueError(
                f"unit {ordinal}: audit intervals do not cover every source line exactly once"
            )

        classes: list[str] = []
        for row in overlaps:
            for value in row["class_normalized"].split(";"):
                value = value.strip()
                if value and value not in classes:
                    classes.append(value)

        output.append(
            {
                "unit_ordinal": str(ordinal),
                "unit_kind": unit["kind"],
                "unit_title": unit["title"],
                "unit_source_label": unit["label"],
                "source_start": str(start),
                "source_end": str(end),
                "source_sha256": unit["sha256"],
                "restoration_provenance_id": "",
                "restoration_record_path": "",
                "restoration_record_sha256": "",
                "authority_path": AUTHORITY_PATH,
                "authority_sha256": source_hash,
                "authority_edition_status": "pending",
                "authority_edition_value": "",
                "presentation_identity_status": "open/missing",
                "presentation_identity_value": "",
                "presentation_identity_description": "",
                "audit_interval_ids": json.dumps(
                    [row["stable_id"] for row in overlaps], ensure_ascii=False
                ),
                "audit_class_evidence": json.dumps(classes, ensure_ascii=False),
                "provenance_disposition": "open/missing",
                "handbook_destination_status": "open/missing",
                "handbook_destination": "",
                "stable_labels": "[]",
                "audit_result": "pending",
                "notation_completeness": "pending",
                "definitions_completeness": "pending",
                "rules_completeness": "pending",
                "side_conditions_completeness": "pending",
                "hypotheses_completeness": "pending",
                "statements_completeness": "pending",
                "proofs_completeness": "pending",
                "examples_completeness": "pending",
                "qualifications_completeness": "pending",
                "attribution_completeness": "pending",
                "source_fidelity_ai_verification": "pending",
                "topic_specialist_ai_verification": "pending",
                "adversarial_publication_ai_verification": "pending",
                "static_verification": "pending",
                "build_verification": "pending",
                "visual_verification": "pending",
            }
        )

    if ordinals != set(range(1, 1056)):
        raise ValueError("inventory unit ordinals are not exactly 1--1055")
    return (
        apply_reviewed_records(
            output, reviewed_records_path, source_hash, repository_root
        ),
        source_hash,
    )


def csv_text(rows: list[dict[str, str]]) -> str:
    buffer = io.StringIO(newline="")
    writer = csv.DictWriter(buffer, fieldnames=OUTPUT_FIELDS, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return buffer.getvalue()


def markdown_text(rows: list[dict[str, str]], source_hash: str) -> str:
    multi = sum(len(json.loads(row["audit_interval_ids"])) > 1 for row in rows)
    reviewed = [
        row for row in rows if row["authority_edition_status"] != "pending"
    ]
    passing = [
        row
        for row in reviewed
        if row["provenance_disposition"] == PASSING_DISPOSITION
    ]
    open_rows = [
        row for row in rows if row["provenance_disposition"] == "open/missing"
    ]
    if reviewed:
        reviewed_open = [
            row
            for row in reviewed
            if row["provenance_disposition"] == OPEN_DISPOSITION
        ]
        restoration_ids = {
            row["restoration_provenance_id"]
            for row in reviewed
            if row["restoration_provenance_id"]
        }
        review_summary = [
            f"- Reviewer-supplied records accepted: {len(reviewed):,}.",
            f"- Unit-bearing restoration records represented: {len(restoration_ids):,}.",
            f"- Units with disposition `{PASSING_DISPOSITION}`: {len(passing):,}.",
            f"- Admitted units still open: {len(reviewed_open):,}.",
            f"- Units retaining disposition `open/missing`: {len(open_rows):,}.",
            "- An open record may expose checked identity, provenance, destination,",
            "  audit, completeness, and verification results without closing the unit.",
            "- A non-open disposition is admitted only when all completeness and",
            "  verification results pass and every verification category has evidence.",
        ]
        corrected_count = sum(row["provenance_disposition"] == CORRECTED_DISPOSITION for row in reviewed)
        if corrected_count:
            review_summary.insert(3, f"- Units with validated corrected-reader disposition `{CORRECTED_DISPOSITION}`: {corrected_count:,}.")
        outstanding_summary = [
            "Any unresolved typed destination, stable-label, authority-edition,",
            "presentation-identity, completeness, or independent-verification value",
            "remains owed for a row retaining disposition `open/missing`.",
        ]
    else:
        # Preserve the original zero-review summary byte-for-byte so adding the
        # empty governed input does not churn the generated historical baseline.
        review_summary = [
            "- Current provenance disposition on every unit: `open/missing`.",
            "- Current destination status on every unit: `open/missing`.",
            "- Authority-edition value on every unit: blank; identification status:",
            "  `pending`.",
            "- Presentation-identity value and description on every unit: blank;",
            "  identity status: `open/missing`.",
            "- All ten required completeness dimensions: `pending`.",
            "- Every verification result: `pending`.",
        ]
        outstanding_summary = [
            "Typed handbook destinations, stable labels, authority-edition values,",
            "presentation-identity values/descriptions, and independent",
            "source-fidelity AI, topic-specialist AI, adversarial-publication AI,",
            "static, build, and visual evidence remain owed.",
        ]
    return "\n".join(
        [
            "# Source-unit to audit-interval crosswalk",
            "",
            "This generated administrative crosswalk joins every active named inherited",
            "source unit to the exhaustive interval-audit baseline. It makes no claim that",
            "a unit has been transcribed, reconstructed, or assigned a valid destination.",
            "",
            f"- Authority: `source/formal-logic-reference.tex`.",
            f"- Authority SHA-256: `{source_hash}`.",
            f"- Active source units: {len(rows):,}.",
            f"- Units crossing more than one audit interval: {multi:,}.",
            "- Units lacking exact single line coverage by audit intervals: 0.",
            *review_summary,
            "",
            "The companion CSV is the complete unit crosswalk. Audit classes are evidence",
            "inherited from overlapping interval rows, not an inferred unit-level PASS.",
            *outstanding_summary,
            "",
        ]
    )


def write_or_check(path: Path, content: str, check: bool) -> None:
    encoded = content.encode("utf-8")
    if check:
        if not path.is_file() or path.read_bytes() != encoded:
            raise ValueError(f"stale generated artifact: {path}")
    else:
        path.write_bytes(encoded)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--inventory", type=Path, default=DEFAULT_INVENTORY)
    parser.add_argument("--audit-map", type=Path, default=DEFAULT_AUDIT_MAP)
    parser.add_argument("--source", type=Path, default=DEFAULT_SOURCE)
    parser.add_argument(
        "--reviewed-records", type=Path, default=DEFAULT_REVIEWED_RECORDS
    )
    parser.add_argument(
        "--repository-root",
        type=Path,
        default=ROOT,
        help="root for repository-relative destination and evidence paths",
    )
    parser.add_argument("--csv", type=Path, default=DEFAULT_CSV)
    parser.add_argument("--markdown", type=Path, default=DEFAULT_MD)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument(
        "--write",
        action="store_true",
        help="write the canonical CSV and Markdown artifacts (the default mode)",
    )
    mode.add_argument("--check", action="store_true")
    args = parser.parse_args()

    rows, source_hash = build_rows(
        args.inventory,
        args.audit_map,
        args.source,
        args.reviewed_records,
        args.repository_root,
    )
    csv_output = csv_text(rows)
    md_output = markdown_text(rows, source_hash)
    write_or_check(args.csv, csv_output, args.check)
    write_or_check(args.markdown, md_output, args.check)
    action = "verified" if args.check else "wrote"
    open_units = sum(
        row["provenance_disposition"] == OPEN_DISPOSITION for row in rows
    )
    reviewed_units = sum(
        row["authority_edition_status"] != "pending" for row in rows
    )
    suffix = f", {reviewed_units} reviewed" if reviewed_units else ""
    print(
        f"{action} source-unit audit crosswalk: {open_units} open units{suffix}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
