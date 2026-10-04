#!/usr/bin/env python3
"""Generate the LaTeX table bodies of the gap-analysis document from the
CSV registers (the single source of truth) and the v1.0 manuscript.

Usage: python tools/csv2tex.py
Writes spec/generated/*.tex. Cells are LaTeX-valued by convention (the
registers escape their own specials), so no escaping happens here.
"""

import csv
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REG = ROOT / "spec" / "registers"
OUT = ROOT / "spec" / "generated"
SOURCE = ROOT / "source" / "formal-logic-reference.tex"


def write_output(path: Path, text: str) -> None:
    with path.open("w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)


def rows(name: str) -> list[dict]:
    path = REG / name
    if not path.exists():
        print(f"[csv2tex] missing register: {path}", file=sys.stderr)
        sys.exit(1)
    with path.open(encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh))


def longtable(colspec: str, header: list[str], body_rows: list[list[str]],
              size: str = r"\scriptsize") -> str:
    head = " & ".join(rf"\textbf{{{h}}}" for h in header) + r" \\"
    lines = [
        r"\begingroup" + size + r"\setlength{\tabcolsep}{3pt}",
        rf"\begin{{longtable}}{{{colspec}}}",
        r"\toprule", head, r"\midrule", r"\endfirsthead",
        r"\toprule", head, r"\midrule", r"\endhead",
        r"\midrule\multicolumn{" + str(len(header)) +
        r"}{r}{\emph{continued}}\\\endfoot",
        r"\bottomrule\endlastfoot",
    ]
    for r in body_rows:
        lines.append(" & ".join(r) + r" \\")
    lines += [r"\end{longtable}", r"\endgroup"]
    return "\n".join(lines) + "\n"


DISP_ABBREV = {"FIX-SOURCE": "FIX", "RESOLVE-BY-MIGRATION": "MIGR",
               "OBSOLETE": "OBS", "CARRY": "CARRY"}


def gen_defects() -> None:
    data = rows("defects.csv")
    body = [[r["id"], r["priority"], r["v1_lines"], r["finding"],
             r["required_fix"], DISP_ABBREV.get(r["disposition"], r["disposition"]),
             r["phase"], r["status"]] for r in data]
    write_output(OUT / "defects-table.tex", longtable(
        r"@{}p{0.45in}p{0.25in}p{0.7in}p{2.2in}p{1.75in}p{0.45in}p{0.16in}p{0.34in}@{}",
        ["ID", "Pri", "v1.0 lines", "Finding", "Required fix", "Disp", "Ph", "St"],
        body))


def gen_depth() -> None:
    data = rows("depth-gaps.csv")
    body = [[r["id"], r["item"], r["target_home"], r["treatment"],
             r["priority"], r["notes"]] for r in data]
    write_output(OUT / "depth-table.tex", longtable(
        r"@{}p{0.62in}p{2.6in}p{0.75in}p{0.22in}p{0.42in}p{1.85in}@{}",
        ["ID", "Item", "Target", "Tr", "Prio", "Notes"],
        body))


def gen_newcontent() -> None:
    data = rows("new-content.csv")
    body = [[r["id"], f'{r["target_part"]} {r["chapter"]}', r["item"],
             r["treatment"], r["priority"], r["sources"]] for r in data]
    write_output(OUT / "newcontent-table.tex", longtable(
        r"@{}p{0.52in}p{0.85in}p{2.5in}p{0.22in}p{0.42in}p{1.95in}@{}",
        ["ID", "Target", "Item", "Tr", "Prio", "Sources"],
        body))


def gen_apparatus() -> None:
    data = rows("apparatus.csv")
    body = [[r["id"], r["category"], r["item"], r["spec"], r["priority"],
             r["phase"]] for r in data]
    write_output(OUT / "apparatus-table.tex", longtable(
        r"@{}p{0.45in}p{0.78in}p{2.02in}p{2.6in}p{0.42in}p{0.16in}@{}",
        ["ID", "Category", "Item", "Specification", "Prio", "Ph"],
        body))


def tab(counter: Counter, title: str, key_head: str) -> str:
    lines = [rf"\begin{{tabular}}[t]{{@{{}}lr@{{}}}}",
             rf"\multicolumn{{2}}{{@{{}}l@{{}}}}{{\textbf{{{title}}}}}\\",
             r"\midrule"]
    for k, v in sorted(counter.items()):
        lines.append(rf"{k} & {v} \\")
    lines.append(rf"\midrule total & {sum(counter.values())} \\")
    lines.append(r"\end{tabular}")
    return "\n".join(lines)


def gen_dashboard() -> None:
    d = rows("defects.csv")
    g = rows("depth-gaps.csv")
    n = rows("new-content.csv")
    a = rows("apparatus.csv")
    blocks = [
        tab(Counter(r["class"] for r in d), "Defects by class", "class"),
        tab(Counter(r["priority"] for r in d), "Defects by priority", "pri"),
        tab(Counter(r["disposition"] for r in d), "Defects by disposition", "disp"),
        tab(Counter(r["treatment"] for r in g), "Depth gaps by treatment", "tr"),
        tab(Counter(r["priority"] for r in g), "Depth gaps by priority", "pri"),
        tab(Counter(r["domain"] for r in n), "New content by domain", "dom"),
        tab(Counter(r["treatment"] for r in n if r["domain"] != "x"),
            "New content by treatment", "tr"),
        tab(Counter(r["category"] for r in a), "Apparatus by category", "cat"),
    ]
    body = ("\n\\quad\n".join(blocks[:3]) + "\n\n\\medskip\n\n" +
            "\n\\quad\n".join(blocks[3:5]) + "\n\\quad\n" + blocks[5] +
            "\n\n\\medskip\n\n" + blocks[6] + "\n\\quad\n" + blocks[7])
    totals = (f"Register totals: {len(d)} defects, {len(g)} depth gaps, "
              f"{len(n)} new-content rows "
              f"({sum(1 for r in n if r['domain'] != 'x')} in-scope, "
              f"{sum(1 for r in n if r['domain'] == 'x')} recorded exclusions), "
              f"{len(a)} apparatus items --- "
              f"{len(d) + len(g) + len(n) + len(a)} register rows in all.")
    write_output(OUT / "dashboard.tex",
        "\\noindent " + totals + "\n\n\\medskip\n\n\\noindent\\begingroup\\scriptsize\n"
        + body + "\n\\endgroup\n")


def gen_toc() -> None:
    text = SOURCE.read_text(encoding="utf-8", errors="replace")
    body_rows = []
    part_re = re.compile(r"^\\part\{([^}]*)\}")
    chap_re = re.compile(r"^\\chapter(?:\[([^\]]*)\])?\{([^}]*)\}")
    for i, line in enumerate(text.splitlines(), start=1):
        m = part_re.match(line)
        if m:
            body_rows.append([rf"\textbf{{{m.group(1)}}}", "", str(i)])
            continue
        m = chap_re.match(line)
        if m:
            title = m.group(1) if m.group(1) else m.group(2)
            body_rows.append(["", title, str(i)])
    write_output(OUT / "toc-v1.tex", longtable(
        r"@{}p{2.1in}p{3.6in}p{0.6in}@{}",
        ["Part", "Chapter", "Line"], body_rows, size=r"\footnotesize"))


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    gen_defects()
    gen_depth()
    gen_newcontent()
    gen_apparatus()
    gen_dashboard()
    gen_toc()
    print(f"[csv2tex] wrote {len(list(OUT.glob('*.tex')))} files to {OUT}")


if __name__ == "__main__":
    main()
