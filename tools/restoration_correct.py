#!/usr/bin/env python3
"""Record lead corrections to restoration captures as version-4 corrected-reader records.

Under the correction policy (spec/EDITION-2026-CONTRACT.md, "Reader-facing content and
corrections"; handbook/CONVENTIONS.md 2026-09-06) the lead may correct an active restoration
capture handbook/restoration/inherited-NNNNN-MMMMM.tex. The capture's provenance record
spec/provenance/<ID>.json must then describe the correction, or check.py flags the scope as
stale. For each named record whose artifact bytes changed, this tool:

1. copies the current record to spec/provenance/history/<ID>.v<version>-<sha8>.json
   (the predecessor; version 1 or 4 only, as the checker requires);
2. recomputes the complete edit map of the current capture against the frozen source
   interval (every changed line range, with slice digests);
3. writes the record as schema version 4 with a reader_correction block naming the policy,
   the rationale file (one "## <ID>" section per record) and the predecessor;
4. validates it with tools/check_inherited_restoration.py and restores the old record (and
   removes the history copy) if validation fails.

Without --apply it only reports what would change. Records with other schema versions
(e.g. 3, appendix-layout captures) are refused.

Usage: python -B tools/restoration_correct.py --rationale spec/research/X.md
           --correction-id ID [--affected ID ...] [--reasons REASONS.json] [--apply] RECORD_ID...
REASONS.json maps record id -> one reason string used for each of its edits.
"""
from __future__ import annotations

import argparse
import difflib
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import check_inherited_restoration as checker  # noqa: E402


def digest(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def build(pid: str, args: argparse.Namespace, reasons: dict[str, str]) -> tuple[dict, bytes, Path] | str:
    """The new record, the predecessor bytes and the history path; or a reason it is skipped."""
    record_path = ROOT / "spec" / "provenance" / f"{pid}.json"
    raw = record_path.read_bytes()
    rec = json.loads(raw)
    version = rec.get("schema_version")
    if version not in (1, 4):
        return f"schema version {version} cannot take a corrected-reader record"
    artifact_path = ROOT / rec["restoration_artifact"]["path"]
    reader_raw = artifact_path.read_bytes()
    if digest(reader_raw) == rec["restoration_artifact"]["sha256"]:
        return "artifact unchanged"
    authority = ROOT / rec["authority"]["path"]
    source_lines = checker.physical_lines(authority.read_bytes(), str(authority))
    start, end = rec["source_locator"]["start_line"], rec["source_locator"]["end_line"]
    original = checker.correction_slice_bytes(source_lines[start - 1:end], pid)
    reader_lines = checker.physical_lines(reader_raw, rel(artifact_path))
    current = checker.correction_slice_bytes(reader_lines, rel(artifact_path))
    before, after = original.splitlines(keepends=True), current.splitlines(keepends=True)
    reason = reasons.get(pid) or f"Lead correction recorded in {args.rationale}, section {pid}."
    edits = []
    for tag, i, j, a, b in difflib.SequenceMatcher(None, before, after, autojunk=False).get_opcodes():
        if tag == "equal":
            continue
        edits.append({"source_range": [i, j], "reader_range": [a, b],
                      "source_sha256": digest(b"".join(before[i:j])),
                      "reader_sha256": digest(b"".join(after[a:b])),
                      "reason": reason})
    history = ROOT / "spec" / "provenance" / "history" / f"{pid}.v{version}-{digest(raw)[:8]}.json"
    affected = set(args.affected) | {pid}
    if version == 4:
        affected |= set(rec["reader_correction"]["affected_ids"])
    rationale = ROOT / args.rationale
    policy = ROOT / checker.CORRECTION_POLICY_PATH
    new = dict(rec)
    new["schema_version"] = 4
    new["presentation_identity"] = {**rec["presentation_identity"], "kind": "corrected reader source interval"}
    if version == 1:
        new["presentation_identity"]["description"] = (
            "The source presentation retains every original line outside the explicitly mapped "
            "correction edits; it is a corrected reader presentation, not unchanged transcription.")
        new["owed_artifacts"] = [
            "Preserve the frozen source byte for byte and every original reader line outside the explicitly mapped edits.",
            "Verify the corrected statements and navigation at their exact scopes; preserve all original labels, statements and proof content.",
            "Complete every applicable content and independent AI gate, completeness dimension, build, visual and human-review obligation through the separate admission records."]
    new["restoration_artifact"] = {
        "path": rec["restoration_artifact"]["path"], "bytes": len(reader_raw),
        "physical_lines": len(reader_lines), "sha256": digest(reader_raw),
        "content_token_sha256": digest(current),
        "content_token_comparison": checker.CORRECTED_CONTENT_COMPARISON}
    new["disposition"] = "full reconstruction"
    new["verification_evidence"] = [{**e, "scope": checker.CORRECTION_VERIFICATION_SCOPES[e["kind"]]}
                                    for e in rec["verification_evidence"]]
    new["reader_correction"] = {
        "kind": "candidate corrected reader interval",
        "correction_id": args.correction_id,
        "policy_authority": {"path": checker.CORRECTION_POLICY_PATH, "sha256": digest(policy.read_bytes()),
                             "locator": checker.CORRECTION_POLICY_LOCATOR},
        "rationale": {"path": args.rationale, "sha256": digest(rationale.read_bytes()), "locator": pid},
        "predecessor_record": {"path": rel(history), "sha256": digest(raw)},
        "affected_ids": sorted(affected),
        "source_content_token_sha256": digest(original),
        "edits": edits}
    return new, raw, history


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--rationale", required=True)
    ap.add_argument("--correction-id", required=True)
    ap.add_argument("--affected", action="append", default=[])
    ap.add_argument("--reasons")
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("records", nargs="+")
    args = ap.parse_args()
    rationale_text = (ROOT / args.rationale).read_text(encoding="utf-8")
    reasons = json.loads((ROOT / args.reasons).read_text(encoding="utf-8")) if args.reasons else {}
    failed = 0
    for pid in args.records:
        if f"## {pid}" not in rationale_text:
            print(f"{pid}: refused: rationale has no '## {pid}' section")
            failed += 1
            continue
        out = build(pid, args, reasons)
        if isinstance(out, str):
            print(f"{pid}: skipped: {out}")
            failed += out != "artifact unchanged"
            continue
        new, old_raw, history = out
        n = len(new["reader_correction"]["edits"])
        if not args.apply:
            print(f"{pid}: would record {n} edits (predecessor {rel(history)})")
            continue
        record_path = ROOT / "spec" / "provenance" / f"{pid}.json"
        history.parent.mkdir(parents=True, exist_ok=True)
        history.write_bytes(old_raw)
        record_path.write_text(json.dumps(new, indent=2, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")
        try:
            checker.validate_record(checker.load_json(record_path), record_path, ROOT)
        except Exception as exc:  # fail closed: restore the old record
            record_path.write_bytes(old_raw)
            history.unlink()
            print(f"{pid}: REFUSED by check_inherited_restoration ({exc}); record restored")
            failed += 1
            continue
        print(f"{pid}: recorded {n} edits; validated")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
