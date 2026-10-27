#!/usr/bin/env python3
"""Generate the complete live theorem/lemma index from the reader route."""

from __future__ import annotations

import argparse
import csv
import re
from pathlib import Path

import check as hbcheck


ROOT = Path(__file__).resolve().parents[1]
HANDBOOK = ROOT / "handbook"
OUTPUT = HANDBOOK / "generated" / "named-theorem-index.tex"
HOOKED_SOURCE_RESULTS = {
    "thm:algebraically-closed-fields": ("Algebraically closed fields", "Theorem"),
    "thm:ryll-nardzewski": ("Ryll--Nardzewski", "Theorem"),
    "thm:morley-categoricity": ("Morley's categoricity theorem", "Theorem"),
    "thm:machine-decidability": ("Machine form of decidability", "Lemma"),
    "thm:ce-equivalent-forms": ("Equivalent forms of computable enumerability", "Theorem"),
    "thm:trakhtenbrot": ("Trakhtenbrot", "Theorem"),
    "thm:arithmetical-hierarchy-classification": ("Hierarchy classifications of program domains and totality", "Theorem"),
    "thm:arithmetical-hierarchy-strictness": ("Strictness of the arithmetical hierarchy", "Theorem"),
    "thm:post-hierarchy": ("Post's theorem", "Theorem"),
    "thm:arithmetization-syntax": ("Arithmetization of syntax", "Theorem"),
    "thm:theoremhood-undecidable": ("Undecidability of theoremhood", "Corollary"),
    "thm:p06-ordered-pair": ("Ordered-pair identity", "Lemma"),
    "thm:p06-set-recursion": ("Set recursion", "Theorem"),
    "thm:p06-ordinal-trichotomy": ("Trichotomy and transitivity of ordinals", "Theorem"),
    "thm:p06-transfinite-induction": ("Transfinite induction", "Theorem"),
    "thm:p06-transfinite-recursion": ("Transfinite recursion", "Theorem"),
    "thm:p06-hierarchy": ("Hierarchy theorem", "Theorem"),
    "thm:p06-mostowski-collapse": ("Mostowski collapse", "Theorem"),
    "thm:p06-hartogs": ("Hartogs", "Theorem"),
    "thm:p06-choice-equivalents-source": ("Equivalent forms of the Axiom of Choice", "Theorem"),
    "thm:p06-constructible-class": ("The constructible class L", "Theorem"),
    "thm:p06-generic-filter-existence": ("Existence of a generic filter under the fixed hypothesis", "Lemma"),
    "thm:p06-semantic-forcing-monotone": ("Monotonicity of semantic forcing", "Lemma"),
}

PART7_HOOKED_SOURCE_RESULTS = {
    ("inherited-11599-11627.tex", "theorem", r"Soundness of \(\LK\)"):
        ("thm:p07-source-lk-soundness", r"Soundness of \(\mathsf{LK}\)", "Theorem"),
    ("inherited-11768-11823.tex", "theorem", r"Cut elimination for \(\LK\) and \(\LJ\)"):
        ("thm:p07-source-cut-elimination", r"Cut elimination for \(\mathsf{LK}\) and \(\mathsf{LJ}\)", "Theorem"),
    ("inherited-11824-11881.tex", "corollary", "Propositional subformula property"):
        ("thm:p07-source-propositional-subformula", "Propositional subformula property", "Corollary"),
    ("inherited-11824-11881.tex", "corollary", "Underivability of the empty sequent"):
        ("thm:p07-source-empty-sequent", "Underivability of the empty sequent", "Corollary"),
    ("inherited-11961-12029.tex", "theorem", "Normalization with empty discharge classes"):
        ("thm:p07-source-nj-normalization", "Normalization with empty discharge classes", "Theorem"),
    ("inherited-12030-12100.tex", "theorem", "Subject reduction"):
        ("thm:p07-source-stlc-subject-reduction", "Subject reduction", "Theorem"),
    ("inherited-12030-12100.tex", "theorem", "Strong normalization"):
        ("thm:p07-source-stlc-strong-normalization", "Strong normalization", "Theorem"),
}

PART8_HOOKED_SOURCE_RESULTS = {
    ("inherited-13046-13057.tex", "lemma", "Persistence"):
        ("thm:p08-source-persistence", "Persistence", "Lemma"),
    ("inherited-13058-13099.tex", "theorem", r"Soundness and strong completeness of \(\IPL\)"):
        ("thm:p08-source-ipl-adequacy", r"Soundness and strong completeness of \(\mathsf{IPL}\)", "Theorem"),
    ("inherited-13285-13316.tex", "theorem", "Frame correspondence and completeness"):
        ("thm:p08-source-modal-four-adequacy", "Frame correspondence and completeness", "Theorem"),
    ("inherited-13440-13471.tex", "theorem", "Soundness and completeness of linear temporal logic"):
        ("thm:p08-source-ltl-adequacy", "Soundness and completeness of linear temporal logic", "Theorem"),
    ("inherited-13519-13551.tex", "theorem", r"Multi-agent \(\Sfive\)"):
        ("thm:p08-source-s5n-adequacy", r"Multi-agent \(\mathsf{S5}\)", "Theorem"),
    ("inherited-13641-13699.tex", "theorem", "Finite-matrix tableau soundness and completeness"):
        ("thm:p08-source-finite-matrix-adequacy", "Finite-matrix tableau soundness and completeness", "Theorem"),
    ("inherited-14001-14015.tex", "theorem", "Soundness, completeness, and cut elimination"):
        ("thm:p08-source-imll-adequacy", "Soundness, completeness, and cut elimination", "Theorem"),
}


def reachable_files() -> list[Path]:
    queue = [HANDBOOK / "main.tex"]
    seen: set[Path] = set()
    ordered: list[Path] = []
    while queue:
        path = queue.pop(0).resolve()
        if path in seen or not path.is_file():
            continue
        seen.add(path)
        ordered.append(path)
        body = hbcheck.strip_verbatims(
            hbcheck.strip_comments(path.read_text(encoding="utf-8"))
        )
        for match in re.finditer(r"\\input\s*\{([^{}]+)\}", body):
            rel = match.group(1).strip()
            if not rel.endswith(".tex"):
                rel += ".tex"
            queue.append(HANDBOOK / rel)
    return ordered


def inventory_titles() -> dict[str, str]:
    with (ROOT / "spec" / "source-unit-inventory.csv").open(
        encoding="utf-8", newline=""
    ) as handle:
        return {
            row["label"]: row["title"]
            for row in csv.DictReader(handle)
            if row["kind"] in {"theorem", "lemma"} and row["label"]
        }


def title_parts(title: str) -> tuple[str, str]:
    depth = 0
    in_math = False
    index = 0
    while index < len(title):
        if title.startswith((r"\(", r"\["), index):
            in_math = True
            index += 2
            continue
        if title.startswith((r"\)", r"\]"), index):
            in_math = False
            index += 2
            continue
        char = title[index]
        if char == "\\":
            index += 2
            continue
        if char == "$":
            in_math = not in_math
        elif char == "{":
            depth += 1
        elif char == "}":
            depth = max(0, depth - 1)
        elif char == "@" and depth == 0 and not in_math:
            return title[:index], title[index + 1 :]
        index += 1
    return title, title


def sort_text(title: str) -> str:
    text = re.sub(r"\\[A-Za-z@]+\*?", " ", title_parts(title)[0])
    return re.sub(r"[^A-Za-z0-9]+", " ", text).strip().casefold()


def detail(status: str, source: bool) -> str:
    if source:
        return "reader-facing source proof/status"
    match = re.fullmatch(r"(proved|sketched)=(annex:[A-Za-z0-9._-]+)", status)
    if match:
        label = match.group(2)
        noun = "annex proof" if match.group(1) == "proved" else "annex sketch"
        return rf"\hyperref[{label}]{{{noun}}}, p.~\pageref{{{label}}}"
    if status.startswith("cited="):
        return rf"source \cite{{{status.removeprefix('cited=')}}}"
    raise ValueError(f"unsupported result status: {status}")


def collect() -> list[tuple[str, str, str, str]]:
    titles = inventory_titles()
    found: list[tuple[str, str, str, str]] = []
    labels: set[str] = set()
    for path in reachable_files():
        body = hbcheck.strip_verbatims(
            hbcheck.strip_comments(path.read_text(encoding="utf-8"))
        )
        for match in re.finditer(r"\\begin\{(hbtheorem|hblemma|hbcorollary)\}", body):
            args, _ = hbcheck.scan_braced_args(body, match.end(), 3)
            if len(args) != 3:
                raise ValueError(f"malformed result in {path}")
            label, status, title = (arg.strip() for arg in args)
            kind = {
                "hbtheorem": "Theorem",
                "hblemma": "Lemma",
                "hbcorollary": "Corollary",
            }[match.group(1)]
            if label in labels:
                raise ValueError(f"duplicate live result label: {label}")
            labels.add(label)
            found.append((title, kind, label, detail(status, False)))
        for match in re.finditer(
            r"\\begin\{(theorem|lemma|corollary)\}(?:\[([^\]]*)\])?", body
        ):
            end_token = rf"\end{{{match.group(1)}}}"
            end = body.find(end_token, match.end())
            if end < 0:
                raise ValueError(f"unterminated source result in {path}")
            label_match = re.search(r"\\label\{([^{}]+)\}", body[match.end():end])
            if not label_match:
                source_key = (path.name, match.group(1), (match.group(2) or "").strip())
                source = (PART7_HOOKED_SOURCE_RESULTS.get(source_key)
                          or PART8_HOOKED_SOURCE_RESULTS.get(source_key))
                interval = re.fullmatch(r"inherited-(\d{5})-(\d{5})\.tex", path.name)
                in_part7 = bool(interval and 11354 <= int(interval.group(1)) <= 12218)
                in_part8 = bool(interval and 12970 <= int(interval.group(1)) <= 14069)
                if not source:
                    if in_part7 or in_part8:
                        raise ValueError(f"unanchored live Part VII/VIII source result: {source_key}")
                    continue
                label, title, kind = source
                if label in labels:
                    raise ValueError(f"duplicate governed source-theorem anchor: {label}")
                labels.add(label)
                found.append((title, kind, label, detail("", True)))
                continue
            label = label_match.group(1).strip()
            if label in labels:
                continue
            labels.add(label)
            title = titles.get(label, label)
            kind = {
                "theorem": "Theorem",
                "lemma": "Lemma",
                "corollary": "Corollary",
            }[match.group(1)]
            found.append((title, kind, label, detail("", True)))
    route_text = "\n".join(
        (HANDBOOK / "parts" / part).read_text(encoding="utf-8")
        for part in ("p03.tex", "p04.tex", "p05.tex", "p06.tex", "p07.tex", "p08.tex")
    )
    route_text += (HANDBOOK / "parts" / "p08" / "source-anchors.tex").read_text(
        encoding="utf-8"
    )
    for label, _, _ in PART7_HOOKED_SOURCE_RESULTS.values():
        if rf"\label{{{label}}}" not in route_text:
            raise ValueError(f"missing governed Part VII source-theorem anchor: {label}")
    for label, _, _ in PART8_HOOKED_SOURCE_RESULTS.values():
        if rf"\label{{{label}}}" not in route_text:
            raise ValueError(f"missing governed Part VIII source-theorem anchor: {label}")
    for label, (title, kind) in HOOKED_SOURCE_RESULTS.items():
        if rf"\label{{{label}}}" not in route_text:
            raise ValueError(f"missing governed source-theorem anchor: {label}")
        if label in labels:
            raise ValueError(f"duplicate governed source-theorem anchor: {label}")
        labels.add(label)
        found.append((title, kind, label, detail("", True)))
    return sorted(found, key=lambda row: (sort_text(row[0]), row[1], row[2]))


def render(rows: list[tuple[str, str, str, str]]) -> bytes:
    lines = [
        "% Generated from every live hbtheorem/hblemma and restored theorem/lemma.",
    ]
    for title, kind, label, proof in rows:
        display_title = title_parts(title)[1]
        lines.append(
            rf"\hyperref[{label}]{{{display_title}}} & {kind} & "
            rf"p.~\pageref{{{label}}} & {proof} \\"
        )
    return ("\n".join(lines) + "\n").encode("utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--write", action="store_true")
    mode.add_argument("--check", action="store_true")
    args = parser.parse_args()
    rows = collect()
    if not rows:
        raise SystemExit("no live theorem/lemma rows found")
    output = render(rows)
    if args.write:
        OUTPUT.write_bytes(output)
    elif not OUTPUT.exists() or OUTPUT.read_bytes() != output:
        raise SystemExit("named-theorem index is stale")
    print(f"named-theorem index: {len(rows)} live theorem/lemma rows")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
