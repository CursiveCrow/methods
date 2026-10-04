"""Faithful numeric-scope migration (TOOLING-SPEC section 8).

Replaces every numeric PNN.k / PNN.k-PMM.j / PNN-PMM scope and every numeric
first_use in handbook/registry/symbols.csv with named scopes bound in
symbol-scopes.json to exactly the reader regions the numeric scope meant in the
frozen baseline capture: the captured chapters' bodies plus the annex items their
results own; for a whole part, the part's driver files (a file holding anything
outside the meaning, such as an annex item owned by another part's result or a
chapter routed after the capture, is replaced by its children and anchors). One
binding per distinct numeric string. Every binding's declarations are compared
with the numeric meaning; any narrowing, or any widening other than unowned
annex headings, refuses --apply. Collisions the rebinding creates (compared with
the numeric scopes evaluated on the capture's chapter identities) are listed as
decision_needed, never resolved here.

Default is a dry run that writes tmp/numeric-migration/dry-run.json only.
Refuses (exit 1, writes nothing) when sha256(symbols.csv) or
sha256(symbol-scopes.json) differs from the capture. --apply additionally needs
--decisions FILE, a JSON object recording the user's decisions:
  {"ghost_reading": "own-file" | "route-order",
   "accepted_collisions": [exact decision_needed strings]}
and writes symbols.csv (lines edited in place) and symbol-scopes.json after
staging both and re-checking both hashes.

Ghost-ordinal readings of P9.k / P10.k (an open user decision; the dry run reports
both against ghost-ordinal-map evidence):
  own-file    the k-th unstarred \\section declared in the monolithic chapter's own
              file (sections hosted in separately input fragment files skipped);
  route-order the k-th unstarred \\section of the chapter in route order, fragment
              files included (the spec's literal wording).
The dry run uses own-file unless --decisions records a reading.
"""
from __future__ import annotations

import argparse
import bisect
import csv
import hashlib
import json
import os
import re
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'tools'))
import symbol_registry as reg  # noqa: E402

BASE = ROOT / 'handbook'
BASELINE = ROOT / 'tmp/edition-2026-coverage-map/batch7-integration/post-actual-five-numeric-baseline.json'
GHOST_MAP = ROOT / 'tmp/edition-2026-coverage-map/ghost-ordinal-map.json'
OUT = ROOT / 'tmp/numeric-migration/dry-run.json'
# Parts whose legacy chapter ordinals became \section units of one monolithic chapter.
SECTION_PARTS = {9, 10}
READINGS = ('own-file', 'route-order')
HEADING_KINDS = set(reg.ReaderIndex.LEVELS) | {'label'}


class Refusal(Exception):
    pass


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    return Path(path).read_text(encoding='utf-8-sig')


def numeric_scope(text):
    interval = reg.parse_scope(text)
    return interval if interval and interval != reg.GLOBAL else None


def stem(label):
    return re.sub(r'^p\d{2}-', '', label.split(':', 1)[1])


def selector_label(sel):
    return sel.get('anchor') or sel.get('from') or sel.get('heading_of')


def benign_extra(d):
    """An unowned annex heading or file label: no result, no chapter of its own."""
    return d.path.startswith('annex/') and not d.owner and d.kind in HEADING_KINDS


def raw_fields(line):
    """Split one CSV line into its raw (still quoted) field texts."""
    fields, cur, quoted = [], [], False
    for ch in line:
        if ch == '"':
            quoted = not quoted
        if ch == ',' and not quoted:
            fields.append(''.join(cur))
            cur = []
        else:
            cur.append(ch)
    fields.append(''.join(cur))
    return fields


def csv_field(value):
    if any(c in value for c in ',"\r\n') or value != value.strip():
        return '"' + value.replace('"', '""') + '"'
    return value


def top_level_split(text):
    """Split a macro cell at commas outside braces, brackets and parentheses."""
    out, cur, depth = [], [], 0
    for ch in text:
        if ch in '{[(':
            depth += 1
        elif ch in '}])':
            depth -= 1
        if ch == ',' and depth == 0:
            out.append(''.join(cur).strip())
            cur = []
        else:
            cur.append(ch)
    out.append(''.join(cur).strip())
    return [t for t in out if t]


def write_files(writes, expected):
    """Stage every file first, re-check the source hashes, then replace each one.

    writes: [(path, text)]; expected: {path: sha256 the file must still have}.
    A refusal or error leaves every target untouched and removes the staged files.
    """
    staged = []
    try:
        for path, text in writes:
            path = Path(path)
            path.parent.mkdir(parents=True, exist_ok=True)
            fd, tmp = tempfile.mkstemp(dir=path.parent, prefix=path.name + '.', suffix='.tmp')
            staged.append((tmp, path))
            with os.fdopen(fd, 'w', encoding='utf-8', newline='\n') as stream:
                stream.write(text)
        for path, digest in expected.items():
            if sha(path) != digest:
                raise Refusal(f'{Path(path).name} changed during the run (sha256 now {sha(path)}); nothing written')
        while staged:
            tmp, path = staged.pop(0)
            os.replace(tmp, path)
    finally:
        for tmp, _ in staged:
            if os.path.exists(tmp):
                os.remove(tmp)


class Cover:
    """Union of [start, end) position pairs, answering membership by bisection."""

    def __init__(self, pairs):
        merged = []
        for start, end in sorted(pairs):
            if merged and start <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], end)
            else:
                merged.append([start, end])
        self.starts = [m[0] for m in merged]
        self.ends = [m[1] for m in merged]

    def __contains__(self, position):
        i = bisect.bisect_right(self.starts, position) - 1
        return i >= 0 and position < self.ends[i]


def span(region):
    return region.start, region.end


def contained(region, regions):
    return any(b.start <= region.start and region.end <= b.end for b in regions)


class Binder:
    """Builds one binding per distinct numeric scope string from the capture."""

    def __init__(self, index, capture, ghost_map, csv_rows, existing, reading):
        self.index = index
        self.reading = reading
        self.chapters = capture['chapters']
        self.by_key = {(c['part'], c['chapter']): c for c in self.chapters}
        self.existing = existing
        self.cache = {}            # numeric string -> binding name
        self.bindings = {}         # name -> {'regions': [...], 'numeric_scopes': [...]}
        self.sections = {}         # (part, reading) -> numbered section labels
        self.lines = {}
        self.diagnostics = {'ghost_evidence_outside_binding': [], 'unlocatable_annex_owners': []}
        # Ghost-map evidence grouped by the CSV scope string of its row.
        self.evidence = {}
        for line, entry in ghost_map.items():
            if entry.get('unresolved'):
                continue
            scope = csv_rows[int(line)]['scope']
            self.evidence.setdefault(scope, []).extend(self.entry_regions(entry))
        self.decls = sorted((d for sites in index.labels.values() for d in sites), key=lambda d: d.start)
        self.starts = [d.start for d in self.decls]
        # Capture chapter identities on the live route; chapters routed after the
        # capture lie inside none of them and had no numeric meaning then.
        self.capture_regions = sorted((index.region(c['selectors'][0]).start, c['part'], c['chapter']) for c in self.chapters)
        captured = Cover(span(index.region(c['selectors'][0])) for c in self.chapters)
        self.post_capture = [h for h in index.heading_records
                             if h.kind == 'chapter' and h.chapter is not None and h.start not in captured]
        self.post_cover = Cover(span(h) for h in self.post_capture)
        # Root (non-annex) owner and capture numeric location of every declaration.
        self.root, self.loc, self.items = {}, {}, []
        for d in self.decls:
            try:
                root = self.root_of(d)
            except reg.RegistryError as exc:
                self.diagnostics['unlocatable_annex_owners'].append(f'{d.label}: {exc}')
                root = d
            self.root[id(d)] = root
            try:
                self.loc[id(d)] = self.capture_location(root)
            except reg.RegistryError:
                self.loc[id(d)] = None
            if d.kind == 'annexitem' and d.owner and root is not d:
                self.items.append(d)
        # An unowned declaration inside an owned annex item (a lemma in its proof, a further
        # \label on the item) is part of that item's reader region: it takes the item's owner.
        item_starts = [a.start for a in self.items]
        for d in self.decls:
            i = bisect.bisect_right(item_starts, d.start) - 1
            if not d.owner and i >= 0 and d.start < self.items[i].end:
                self.root[id(d)], self.loc[id(d)] = self.root[id(self.items[i])], self.loc[id(self.items[i])]

    def root_of(self, d):
        root, seen = d, set()
        while root.owner:
            if root.label in seen:
                raise reg.RegistryError('cyclic annex association: ' + d.label)
            seen.add(root.label)
            root = self.index.unique(root.owner)
        return root

    def capture_location(self, root):
        """part*1000+chapter of the captured chapter holding root; -1 for a post-capture chapter."""
        if root.start in self.post_cover:
            return -1
        if root.part is None or root.chapter is None:
            raise reg.RegistryError(f'no body chapter association for {root.label!r}')
        held = [(p, c) for start, p, c in self.capture_regions if p == root.part and start <= root.start]
        if not held:
            raise reg.RegistryError(f'no captured chapter precedes {root.label!r}')
        return held[-1][0] * 1000 + held[-1][1]

    def inside(self, start, end):
        return self.decls[bisect.bisect_left(self.starts, start):bisect.bisect_left(self.starts, end)]

    def entry_regions(self, entry):
        if entry.get('regions'):
            return entry['regions']
        scope = entry['scope']
        if scope in self.existing:
            return self.existing[scope]['regions']
        if ' through ' in scope:
            first, last = scope.split(' through ')
            return [{'from': first, 'through': last}]
        return [{'anchor': scope}]

    def unique_anchor(self, d):
        return len(self.index.labels.get(d.label, [])) == 1

    def drivers(self, part, meaning):
        """Whole-part selectors: the part's maximal reader files, each used whole only
        when every declaration in it belongs to the meaning; otherwise its child files
        are visited the same way and its own declarations in the meaning are anchored.

        (A part can have top-level files outside its driver, e.g.
        parts/p08/source-anchors.tex input from main.tex, so all maximal files count.)
        """
        files = sorted((sites[0].start, sites[0].end, rel) for rel, sites in self.index.files.items()
                       if rel.startswith(('parts/', 'annex/')) and len(sites) == 1 and sites[0].part == part)
        out = []

        def visit(group):
            reach = -1
            for start, end, rel in sorted(group, key=lambda f: (f[0], -f[1])):
                if end <= reach:
                    continue
                reach = end
                inside = self.inside(start, end)
                if all(id(d) in meaning for d in inside):
                    out.append({'file': rel})
                    continue
                children = [f for f in group if start <= f[0] and f[1] <= end and f[2] != rel]
                visit(children)
                child_cover = Cover((f[0], f[1]) for f in children)
                out.extend({'anchor': d.label} for d in inside
                           if d.start not in child_cover and id(d) in meaning and self.unique_anchor(d))

        visit(files)
        return out

    def regions_for(self, body, whole_parts=(), numbers=()):
        """Selectors for the numeric meaning, and how the selected declarations differ from it.

        Meaning: declarations (annex items via their root owner) in the body selectors or
        in a captured chapter numbered in `numbers`, and, for each whole part, every
        declaration of the part except those in chapters routed after the capture.
        Returns (regions, difference); difference keys: 'missing' (narrowing), 'extra'
        (widening), 'extra_annex_headings' (unowned annex headings in a compressed file).
        """
        index = self.index
        body_cover = Cover(span(index.region(s)) for s in body)
        meaning = set()
        for d in self.decls:
            root, loc = self.root[id(d)], self.loc[id(d)]
            if root.start in body_cover or loc in numbers or (root.part in whole_parts and loc != -1):
                meaning.add(id(d))
        regions = list(body) + [{'anchor': a.label} for a in self.items if id(a) in meaning and self.unique_anchor(a)]
        for part in whole_parts:
            selected = self.drivers(part, meaning)
            files = [index.region(s) for s in selected if 'file' in s]
            # Strict positional containment: a part's last chapter region ends one token
            # past its driver file, so that anchor stays beside the drivers.
            regions = [s for s in regions if not contained(index.region(s), files)] + selected
        # An annex file replaces its anchored items only when everything in it is in the
        # meaning, unowned annex headings aside.
        regions = list({json.dumps(r, sort_keys=True): r for r in regions}.values())
        anchored = [index.unique(s['anchor']) for s in regions if set(s) == {'anchor'}]
        compressible = set()
        for path in {a.path for a in anchored if a.kind == 'annexitem'}:
            sites = index.files.get(path, [])
            if len(sites) == 1 and all(id(d) in meaning or benign_extra(d) for d in self.inside(sites[0].start, sites[0].end)):
                compressible.add(path)
        drop = {a.label for a in anchored if a.kind == 'annexitem' and a.path in compressible}
        regions = [s for s in regions if s.get('anchor') not in drop] + [{'file': p} for p in sorted(compressible)]
        cover = Cover(span(index.region(r)) for r in regions)
        bound = {id(d) for d in self.decls if d.start in cover}
        named = lambda ds: sorted(f'{d.label} ({d.path}:{d.line})' for d in ds)  # noqa: E731
        extra = [d for d in self.decls if id(d) in bound and id(d) not in meaning]
        difference = {
            'missing': named(d for d in self.decls if id(d) in meaning and id(d) not in bound),
            'extra': named(d for d in extra if not benign_extra(d)),
            'extra_annex_headings': named(d for d in extra if benign_extra(d)),
        }
        return regions, {k: v for k, v in difference.items() if v}

    def line_text(self, path, number):
        if path not in self.lines:
            self.lines[path] = (self.index.base / path).read_text(encoding='utf-8-sig').split('\n')
        return self.lines[path][number - 1]

    def numbered_sections(self, part, reading):
        """Labels of the unstarred sections of the part's monolithic first chapter (see module doc)."""
        if (part, reading) in self.sections:
            return self.sections[part, reading]
        chapter = self.by_key.get((part, 1))
        out = []
        if chapter is not None:
            region = self.index.region(chapter['selectors'][0])
            for h in self.index.heading_records:
                if h.kind != 'section' or not region.start <= h.start < region.end:
                    continue
                if reading == 'own-file' and h.path != chapter['path']:
                    continue
                text = self.line_text(h.path, h.line)
                if not re.search(r'\\section\b', text):
                    raise Refusal(f'cannot locate \\section text at {h.path}:{h.line}')
                if re.search(r'\\section\s*\*', text):
                    continue
                labels = [d.label for d in self.inside(h.start, h.start + 1) if d.kind == 'section' and d.path == h.path]
                if not labels:
                    raise Refusal(f'unlabelled numbered section at {h.path}:{h.line}')
                out.append(labels[0])
        self.sections[part, reading] = out
        return out

    def reading_agreement(self):
        """Each single ghost ordinal of P9/P10 with ghost-map evidence: the unit under each reading."""
        out = {}
        for scope, sels in sorted(self.evidence.items()):
            m = re.fullmatch(r'P(\d+)\.(\d+)', scope)
            if not m or int(m[1]) not in SECTION_PARTS or (int(m[1]), int(m[2])) in self.by_key:
                continue
            part, k = int(m[1]), int(m[2])
            labels = sorted({selector_label(s) for s in sels if selector_label(s)})
            row = {'evidence_labels': labels}
            for reading in READINGS:
                sections = self.numbered_sections(part, reading)
                unit = sections[k - 1] if k <= len(sections) else None
                row[reading] = {'unit': unit, 'agrees': unit in labels if unit else 'beyond sections; evidence used'}
            out[scope] = row
        return out

    def ghost_unit(self, part, k):
        """Legacy unit (part, k): ('chapter', chapter) or ('regions', selectors, stem, first, from_evidence)."""
        if part in SECTION_PARTS:
            sections = self.numbered_sections(part, self.reading)
            if k <= len(sections):
                label = sections[k - 1]
                return ('regions', [{'anchor': label}], stem(label), label, False)
        evidence = self.evidence.get(f'P{part}.{k}', [])
        if not evidence:
            raise Refusal(f'ghost ordinal P{part}.{k} has no legacy interpretation or ghost-map evidence')
        if part not in SECTION_PARTS:
            # The current chapter that held the legacy unit.
            held = [c for c in self.chapters if c['part'] == part and c['selectors'][0] in evidence]
            if len(held) != 1:
                raise Refusal(f'ghost ordinal P{part}.{k}: evidence names {len(held)} current chapters')
            return ('chapter', held[0])
        labels = [selector_label(s) for s in evidence if selector_label(s)]
        if not labels:
            raise Refusal(f'ghost ordinal P{part}.{k}: evidence has no declaration label')
        return ('regions', evidence, stem(labels[0]), labels[0], True)

    def first_use(self, token):
        m = reg.FIRST_RE.fullmatch(token)
        part, k = int(m[1]), int(m[2])
        chapter = self.by_key.get((part, k))
        if chapter is None:
            unit = self.ghost_unit(part, k)
            chapter = unit[1] if unit[0] == 'chapter' else None
            if chapter is None:
                return unit[3]
        if not chapter['valid_first_use']:
            raise Refusal(f'chapter P{part}.{k} has no valid first-use declaration')
        return chapter['valid_first_use']

    def name_chapters(self, chosen):
        first, last = chosen[0], chosen[-1]
        a, b = stem(selector_label(first['selectors'][0])), stem(selector_label(last['selectors'][0]))
        if first['part'] == last['part']:
            return f'P{first["part"]} {a}' if len(chosen) == 1 else f'P{first["part"]} {a} to {b}'
        whole_last = sum(1 for c in self.chapters if c['part'] == last['part']) == sum(1 for c in chosen if c['part'] == last['part'])
        name = f'Parts {first["part"]}\u2013{last["part"]} from {a}'
        return name if whole_last else f'{name} to {b}'

    def chapter_binding(self, chosen):
        parts = {c['part'] for c in chosen}
        whole = sorted(p for p in parts if sum(1 for c in self.chapters if c['part'] == p) == sum(1 for c in chosen if c['part'] == p))
        numbers = {c['part'] * 1000 + c['chapter'] for c in chosen}
        return (self.name_chapters(chosen), *self.regions_for([c['selectors'][0] for c in chosen], whole, numbers))

    def bind(self, text):
        if text in self.cache:
            return self.cache[text]
        lo, hi = numeric_scope(text)
        chosen = sorted((c for c in self.chapters if lo <= c['part'] * 1000 + c['chapter'] <= hi), key=lambda c: (c['part'], c['chapter']))
        if chosen:
            name, regions, difference = self.chapter_binding(chosen)
        else:
            name, regions, difference = self.ghost_binding(text, lo, hi)
        named = re.match(r'P(\d+) ', name)
        if named and any(self.index.region(s).part != int(named[1]) for s in regions):
            # An owned annex item hosted in another part's annex: symbol_registry requires a
            # P<n> name to lie wholly in part n, so the single-part name is spelt 'Part <n>'.
            name = 'Part ' + name[1:]
            if name not in self.diagnostics.setdefault('renamed_for_foreign_hosted_annex_items', []):
                self.diagnostics['renamed_for_foreign_hosted_annex_items'].append(name)
        prior = self.bindings.get(name)
        if prior and prior['regions'] != regions:
            raise Refusal(f'binding name {name!r} produced for two different region sets')
        if name in self.existing and self.existing[name]['regions'] != regions:
            raise Refusal(f'binding name {name!r} already exists in symbol-scopes.json with other regions')
        entry = self.bindings.setdefault(name, {'regions': regions, 'numeric_scopes': []})
        entry['numeric_scopes'].append(text)
        if difference:
            entry['coverage_difference'] = difference
        self.cache[text] = name
        return name

    def ghost_binding(self, text, lo, hi):
        part = lo // 1000
        if hi // 1000 != part or lo % 1000 == 0:
            raise Refusal(f'ghost numeric scope {text} is not a range of chapter ordinals in one part')
        ks = list(range(lo % 1000, hi % 1000 + 1))
        units = [self.ghost_unit(part, k) for k in ks]
        if all(u[0] == 'chapter' for u in units):
            chosen = sorted({id(u[1]): u[1] for u in units}.values(), key=lambda c: c['chapter'])
            name, regions, difference = self.chapter_binding(chosen)
            self.check_evidence(text, regions)
            return name, regions, difference
        if any(u[0] == 'chapter' for u in units):
            raise Refusal(f'ghost numeric scope {text} mixes chapter and section units')
        body = [s for u in units for s in u[1]]
        if any(u[4] for u in units):
            body += self.evidence.get(text, [])
        regions, difference = self.regions_for(list({json.dumps(s, sort_keys=True): s for s in body}.values()))
        if not any(u[4] for u in units):
            self.check_evidence(text, regions)
        if len(units) == 1:
            return f'P{part} legacy unit {ks[0]} {units[0][2]}', regions, difference
        return f'P{part} legacy units {ks[0]}\u2013{ks[-1]} {units[0][2]} to {units[-1][2]}', regions, difference

    def check_evidence(self, text, regions):
        """Report ghost-map evidence whose declarations fall outside the legacy-unit binding."""
        cover = Cover(span(self.index.region(s)) for s in regions)
        for sel in self.evidence.get(text, []):
            region = self.index.region(sel)
            outside = sorted({d.label for d in self.inside(region.start, region.end) if d.start not in cover})
            item = {'numeric_scope': text, 'evidence_region': sel, 'declarations_outside': outside}
            if outside and item not in self.diagnostics['ghost_evidence_outside_binding']:
                self.diagnostics['ghost_evidence_outside_binding'].append(item)


class CaptureIndex:
    """The live reader index, but numeric locations come from the capture's chapter identities."""

    def __init__(self, binder):
        self.binder = binder

    def __getattr__(self, name):
        return getattr(self.binder.index, name)

    def numeric_location(self, declaration, seen=None):
        return self.binder.capture_location(self.binder.root_of(declaration))


class Usage:
    """Where a row's distinctive TeX tokens occur in its scope's parts (a heuristic signal).

    An occurrence is placed at the reader position of the nearest preceding declaration
    or heading in the same file (the file start when none precedes it).
    """

    def __init__(self, binder):
        self.binder = binder
        index = binder.index
        strip = reg._grammar().strip_comments
        self.markers = {}
        for d in list(binder.decls) + index.heading_records:
            self.markers.setdefault(d.path, []).append((d.line, d.start))
        for marks in self.markers.values():
            marks.sort()
        self.texts = {}  # part -> [(path, text, file start)]
        for rel, sites in index.files.items():
            if rel.startswith(('parts/', 'annex/')) and len(sites) == 1 and sites[0].part is not None:
                text = strip((index.base / rel).read_text(encoding='utf-8-sig'))
                self.texts.setdefault(sites[0].part, []).append((rel, text, sites[0].start))
        self.found = {}

    def occurrences(self, token, part):
        if (token, part) not in self.found:
            hits = []
            for rel, text, file_start in self.texts.get(part, []):
                at = text.find(token)
                while at >= 0:
                    line = text.count('\n', 0, at) + 1
                    marks = self.markers.get(rel, [])
                    i = bisect.bisect_right(marks, (line, float('inf'))) - 1
                    hits.append((rel, marks[i][1] if i >= 0 else file_start))
                    at = text.find(token, at + len(token))
            self.found[token, part] = hits
        return self.found[token, part]

    def mismatches(self, rebound, bindings):
        """Rows with a distinctive token that occurs in the scope's parts but never inside the
        binding, and rows whose ghost-map evidence lies partly outside the binding."""
        evidence = {e['numeric_scope']: e for e in self.binder.diagnostics['ghost_evidence_outside_binding']}
        covers, out = {}, []
        for item in rebound:
            interval = numeric_scope(item['scope'][0])
            if not interval:
                continue
            name = item['scope'][1]
            if name not in covers:
                covers[name] = Cover(span(self.binder.index.region(s)) for s in bindings[name]['regions'])
            outside, inside = {}, False
            for token in top_level_split(item['macro']):
                if len(token) < 3 or not any(c in token for c in '\\_^{('):
                    continue
                hits = [h for p in range(interval[0] // 1000, interval[1] // 1000 + 1) for h in self.occurrences(token, p)]
                if any(pos in covers[name] for _, pos in hits):
                    inside = True
                elif hits:
                    outside[token] = sorted({rel for rel, _ in hits})
            entry = {}
            if outside:
                entry['tokens_used_only_outside_binding'] = outside
                entry['other_tokens_used_inside_binding'] = inside
            if item['scope'][0] in evidence:
                entry['ghost_evidence_outside_binding'] = evidence[item['scope'][0]]['declarations_outside']
            if entry:
                out.append({'line': item['line'], 'glyph': item['glyph'], 'numeric_scope': item['scope'][0], 'binding': name, **entry})
        return out


def collision_key(error):
    head, _, rest = error.partition(': ')
    kind = 'duplicate glyph-role' if rest.startswith('duplicate glyph-role') else 'glyph-role collision' if rest.startswith('glyph-role collision') else 'error'
    return head, kind


def migrate(base, baseline_path, ghost_map_path, reading='own-file'):
    """Return (report, new_csv_text, new_json_text); raise Refusal on any integrity failure."""
    csv_path = base / 'registry/symbols.csv'
    scopes_path = base / 'registry/symbol-scopes.json'
    capture = json.loads(read(baseline_path))
    hashes = {'symbols.csv': (sha(csv_path), capture['canonical_symbols_sha256']),
              'symbol-scopes.json': (sha(scopes_path), capture['canonical_scopes_sha256'])}
    for name, (current, captured) in hashes.items():
        if current != captured:
            raise Refusal(f'sha256({name}) {current} differs from baseline {captured}')
    csv_text = read(csv_path)
    json_text = read(scopes_path)
    scopes = json.loads(json_text)
    ghost_map = json.loads(read(ghost_map_path)) if Path(ghost_map_path).is_file() else {}

    lines = csv_text.split('\n')
    rows = {}
    for number, line in enumerate(lines, 1):
        if number == 1 or not line:
            continue
        cells = next(csv.reader([line]))
        if len(cells) != len(reg.HEADER) or [next(csv.reader([f]))[0] if f else '' for f in raw_fields(line)] != cells:
            raise Refusal(f'line {number}: cannot edit this CSV line in place')
        rows[number] = dict(zip(reg.HEADER, cells))
    if lines[0].lstrip('\ufeff') != ','.join(reg.HEADER):
        raise Refusal('unexpected symbols.csv header')

    index = reg.ReaderIndex(base)
    binder = Binder(index, capture, ghost_map, rows, scopes['scopes'], reading)
    for item in capture['numeric_rows']:
        lo, hi = item['interval']
        keys = [(c['part'], c['chapter']) for c in item['old_chapters']]
        if keys != [(c['part'], c['chapter']) for c in binder.chapters if lo <= c['part'] * 1000 + c['chapter'] <= hi]:
            raise Refusal(f'capture line {item["canonical_line"]}: old_chapters disagree with the capture chapter list')

    rebound = []
    new_lines = list(lines)
    for number, row in rows.items():
        scope, first = row['scope'], row['first_use']
        new_scope = binder.bind(scope) if numeric_scope(scope) else scope
        new_first = binder.first_use(first) if reg.FIRST_RE.fullmatch(first) else first
        if (new_scope, new_first) == (scope, first):
            continue
        fields = raw_fields(lines[number - 1])
        fields[3], fields[5] = csv_field(new_scope), csv_field(new_first)
        new_lines[number - 1] = ','.join(fields)
        expected = dict(row, scope=new_scope, first_use=new_first)
        if dict(zip(reg.HEADER, next(csv.reader([new_lines[number - 1]])))) != expected:
            raise Refusal(f'line {number}: in-place edit changed other cells')
        rebound.append({'line': number, 'glyph': row['glyph'], 'macro': row['macro'], 'role': row['role'],
                        'scope': [scope, new_scope], 'first_use': [first, new_first]})
    new_csv = '\n'.join(new_lines)

    overrides = []
    new_scopes = json.loads(json_text)
    for name, binding in new_scopes['scopes'].items():
        for item in binding.get('overrides', []):
            if numeric_scope(item['broader_scope']):
                new = binder.bind(item['broader_scope'])
                overrides.append({'scope': name, 'glyph': item['glyph'], 'first_use': item['first_use'], 'broader_scope': [item['broader_scope'], new]})
                item['broader_scope'] = new
    added = {}
    for name, b in binder.bindings.items():
        b['presentation'] = ('Faithful rebinding of legacy numeric scope ' + ', '.join(b['numeric_scopes'])
                             + ': the reader regions it covered in the post-actual-five numeric baseline; not narrowed')
        if name not in new_scopes['scopes']:
            added[name] = {'presentation': b['presentation'], 'regions': b['regions']}
    new_scopes['scopes'].update(added)

    # Text edit of symbol-scopes.json: rewrite numeric broader_scope lines, append new bindings.
    out = []
    for line in json_text.split('\n'):
        m = re.fullmatch(r'(\s*"broader_scope":\s*)"([^"\\]*)"(,?)', line)
        if m and numeric_scope(m[2]):
            line = m[1] + json.dumps(binder.bind(m[2]), ensure_ascii=False) + m[3]
        out.append(line)
    new_json = '\n'.join(out)
    tail = '\n  }\n}\n'
    if not new_json.endswith(tail):
        raise Refusal('symbol-scopes.json does not end with the expected scopes closing')
    if added:
        entries = ',\n'.join('    ' + json.dumps(n, ensure_ascii=False) + ': ' + json.dumps(b, indent=2, ensure_ascii=False).replace('\n', '\n    ')
                             for n, b in added.items())
        new_json = new_json[:-len(tail)] + ',\n' + entries + tail
    if json.loads(new_json) != new_scopes:
        raise Refusal('symbol-scopes.json text edit does not match the intended bindings')

    # Collisions: live numbering (drifted), capture meaning (the baseline), migrated result.
    live_rows, live_errors = reg.read_rows(csv_path, resolver=reg.Resolver(base=base, bindings=scopes, index=index), base=base)
    live_collisions = reg.collision_check(live_rows)
    cap_rows, cap_errors = reg.read_rows(csv_path, resolver=reg.Resolver(base=base, bindings=scopes, index=CaptureIndex(binder)), base=base)
    cap_collisions = reg.collision_check(cap_rows)
    with tempfile.TemporaryDirectory() as tmp:
        tmp_csv = Path(tmp) / 'symbols.csv'
        tmp_csv.write_text(new_csv, encoding='utf-8', newline='\n')
        mig_rows, mig_errors = reg.read_rows(tmp_csv, resolver=reg.Resolver(base=base, bindings=new_scopes, index=index), base=base)
    mig_collisions = reg.collision_check(mig_rows)
    before = {collision_key(e) for e in cap_collisions}
    after = {collision_key(e) for e in mig_collisions}

    still = [r['_line'] for r in mig_rows if numeric_scope(r['scope']) or reg.FIRST_RE.fullmatch(r['first_use'])]
    by_string = {}
    for item in rebound:
        if numeric_scope(item['scope'][0]):
            by_string.setdefault(item['scope'][0], set()).add(item['scope'][1])
    for item in overrides:
        by_string.setdefault(item['broader_scope'][0], set()).add(item['broader_scope'][1])
    split = {k: sorted(v) for k, v in by_string.items() if len(v) != 1}
    differences = {n: b['coverage_difference'] for n, b in sorted(binder.bindings.items()) if 'coverage_difference' in b}
    agreement = binder.reading_agreement()

    report = {
        'symbols_sha256': hashes['symbols.csv'][0],
        'scopes_sha256': hashes['symbol-scopes.json'][0],
        'baseline': str(baseline_path),
        'ghost_reading': reading,
        'rows_rebound_count': len(rebound),
        'rows_still_numeric': still,
        'read_rows_errors': mig_errors,
        'read_rows_errors_capture_meaning': cap_errors,
        'read_rows_errors_live_numbering': live_errors,
        'scope_strings_with_more_than_one_binding': split,
        'coverage': {
            'bindings_narrowed': sorted(n for n, d in differences.items() if 'missing' in d),
            'bindings_widened': sorted(n for n, d in differences.items() if 'extra' in d),
            'bindings_with_annex_heading_extras': sorted(n for n, d in differences.items() if 'extra_annex_headings' in d),
            'annex_heading_extras_reason': ('unowned annex section/file headings inside an annex file compressed '
                                            'because all its items are owned here; they carry no result or chapter'),
            'differences': differences,
        },
        'numeric_scope_bindings': dict(sorted(binder.cache.items())),
        'bindings': {n: binder.bindings[n] for n in sorted(binder.bindings)},
        'override_rewrites': overrides,
        'collision_check': {
            'live_numbering_count': len(live_collisions), 'capture_meaning_count': len(cap_collisions),
            'migrated_count': len(mig_collisions), 'migrated': mig_collisions,
            'capture_meaning': cap_collisions,
            'resolved_by_migration': sorted(e for e in cap_collisions if collision_key(e) not in after),
        },
        'decision_needed': [e for e in mig_collisions if collision_key(e) not in before],
        'ghost_reading_agreement': {
            'readings': {r: f'{sum(1 for a in agreement.values() if a[r]["agrees"] is True)} of '
                            f'{sum(1 for a in agreement.values() if isinstance(a[r]["agrees"], bool))} '
                            f'section-unit ordinals agree with ghost-map evidence' for r in READINGS},
            'ordinals': agreement,
        },
        'usage_meaning_mismatches': Usage(binder).mismatches(rebound, binder.bindings),
        'post_capture_chapters': [f'{h.path}:{h.line}' for h in binder.post_capture],
        'diagnostics': binder.diagnostics,
        'rows_rebound': rebound,
    }
    return report, new_csv, new_json


def load_decisions(path):
    if path is None:
        return {}
    data = json.loads(read(path))
    if (not isinstance(data, dict) or set(data) - {'ghost_reading', 'accepted_collisions', 'note'}
            or data.get('ghost_reading', READINGS[0]) not in READINGS
            or not isinstance(data.get('accepted_collisions', []), list)):
        raise Refusal(f'malformed decisions file {path}')
    return data


def run(base, baseline, ghost_map, out, apply, decisions_path=None):
    try:
        decisions = load_decisions(decisions_path)
        report, new_csv, new_json = migrate(base, baseline, ghost_map, decisions.get('ghost_reading', READINGS[0]))
    except (Refusal, reg.RegistryError, OSError, ValueError) as exc:
        print('REFUSED:', exc)
        return 1
    cov = report['coverage']
    hard = bool(report['rows_still_numeric'] or report['read_rows_errors'] or report['scope_strings_with_more_than_one_binding']
                or cov['bindings_narrowed'] or cov['bindings_widened'])
    accepted = set(decisions.get('accepted_collisions', []))
    open_collisions = [e for e in report['decision_needed'] if e not in accepted]
    reading_open = 'ghost_reading' not in decisions
    print(f'rows rebound: {report["rows_rebound_count"]}; bindings: {len(report["bindings"])}; '
          f'numeric scope strings: {len(report["numeric_scope_bindings"])}; overrides rewritten: {len(report["override_rewrites"])}')
    print(f'rows still numeric: {len(report["rows_still_numeric"])}; read_rows errors: {len(report["read_rows_errors"])} '
          f'(capture meaning {len(report["read_rows_errors_capture_meaning"])}, live numbering {len(report["read_rows_errors_live_numbering"])}); '
          f'strings with >1 binding: {len(report["scope_strings_with_more_than_one_binding"])}')
    print(f'coverage: bindings narrowed (missing): {len(cov["bindings_narrowed"])}; widened (extra): {len(cov["bindings_widened"])}; '
          f'with permitted annex-heading extras: {len(cov["bindings_with_annex_heading_extras"])}')
    for name in cov['bindings_narrowed'] + cov['bindings_widened']:
        print(f'  coverage difference {name}: {cov["differences"][name]}')
    cc = report['collision_check']
    print(f'collisions live numbering/capture meaning/migrated: {cc["live_numbering_count"]}/{cc["capture_meaning_count"]}/{cc["migrated_count"]}; '
          f'decision_needed: {len(report["decision_needed"])} ({len(open_collisions)} not accepted)')
    for item in report['decision_needed']:
        print('  decision_needed:', item, '' if item in open_collisions else '[accepted]')
    print(f'ghost reading: {report["ghost_reading"]} ({"recorded decision" if not reading_open else "DECISION PENDING; spec text reads route-order"}); '
          + '; '.join(f'{r}: {v}' for r, v in report['ghost_reading_agreement']['readings'].items()))
    for item in report['diagnostics']['ghost_evidence_outside_binding']:
        print('  ghost evidence outside binding:', item['numeric_scope'], item['declarations_outside'])
    print(f'post-capture chapters (outside every numeric meaning): {report["post_capture_chapters"]}')
    mismatches = report['usage_meaning_mismatches']
    print(f'usage/meaning mismatches, carried forward unchanged for a later decision (heuristic; details in the report): '
          f'{len(mismatches)} rows')
    groups = {}
    for item in mismatches:
        if 'ghost_evidence_outside_binding' in item:
            why = 'ghost-map evidence ' + ','.join(item['ghost_evidence_outside_binding']) + ' outside binding'
        elif item['other_tokens_used_inside_binding']:
            why = 'some distinctive tokens used only outside binding'
        else:
            why = 'no distinctive token used inside binding'
        groups.setdefault((item['numeric_scope'], item['binding'], why), []).append(str(item['line']))
    for (scope, name, why), lines in groups.items():
        print(f'  {scope} -> {name}: lines {",".join(lines)} ({why})')
    if apply:
        reasons = []
        if hard:
            reasons.append('0 rows still numeric, 0 read_rows errors, one binding per string and exact coverage')
        if open_collisions:
            reasons.append('every decision_needed collision accepted in --decisions')
        if reading_open:
            reasons.append('a ghost_reading recorded in --decisions')
        if reasons:
            print('REFUSED: --apply requires ' + '; '.join(reasons))
            return 1
        try:
            write_files([(base / 'registry/symbols.csv', new_csv), (base / 'registry/symbol-scopes.json', new_json)],
                        {base / 'registry/symbols.csv': report['symbols_sha256'],
                         base / 'registry/symbol-scopes.json': report['scopes_sha256']})
        except Refusal as exc:
            print('REFUSED:', exc)
            return 1
        print('applied: symbols.csv and symbol-scopes.json written')
        return 0
    write_files([(out, json.dumps(report, indent=1, ensure_ascii=False) + '\n')], {})
    print('dry run written:', out)
    return 1 if hard or open_collisions or reading_open else 0


# ---------------------------------------------------------------- selftest

FIXTURE = {
    'main.tex': '\\input{parts/p09}\n\\input{parts/p10}\n\\input{annex/p09}\n\\input{annex/p10}\n',
    'parts/p09.tex': '\\part{Nine}\\label{part:p09}\n\\input{parts/p09/mono}\n\\input{parts/p09/second}\n',
    'parts/p09/mono.tex': ('\\chapter{Mono}\\label{sec:p09-mono}\n'
                           '\\section*{Standing}\\label{sec:p09-standing}\n'
                           '\\section{A}\\label{sec:p09-a}\n\\begin{hbdefinition}{def:p09-a}x\\end{hbdefinition}\n'
                           '\\section{B}\\label{sec:p09-b}\n\\begin{hbdefinition}{def:p09-b}x\\end{hbdefinition}\n'
                           '\\input{parts/p09/fragment}\n'
                           '\\section{C}\\label{sec:p09-c}\n\\begin{hbtheorem}{thm:p09-c}x\\end{hbtheorem}\n'),
    'parts/p09/fragment.tex': '\\section{Fragment}\\label{sec:p09-fragment}\n\\begin{hbdefinition}{def:p09-frag}x\\end{hbdefinition}\n',
    'parts/p09/second.tex': '\\chapter{Second}\\label{sec:p09-second}\n\\begin{hbdefinition}{def:p09-second}uses \\(b_q\\)\\end{hbdefinition}\n',
    'parts/p10.tex': '\\part{Ten}\\label{part:p10}\n\\input{parts/p10/one}\n\\input{parts/p10/two}\n',
    'parts/p10/one.tex': '\\chapter{One}\\label{sec:p10-one}\n\\begin{hbdefinition}{def:p10-one}x\\end{hbdefinition}\n',
    'parts/p10/two.tex': '\\chapter{Two}\\label{sec:p10-two}\n\\begin{hbdefinition}{def:p10-two}x\\end{hbdefinition}\n',
    'annex/p09.tex': '\\input{annex/p09/c}\n\\input{annex/p09/mixed}\n',
    'annex/p09/c.tex': '\\begin{annexitem}{annex:p9.c.1}{thm:p09-c}x\\end{annexitem}\n',
    'annex/p09/mixed.tex': ('\\begin{annexitem}{annex:p9.a.1}{def:p09-a}x\\end{annexitem}\n'
                            '\\begin{annexitem}{annex:p9.s.1}{def:p09-second}x\\end{annexitem}\n'),
    # annex:p10.x.1 is hosted in the P10 annex but owned by a P9.1 result.
    'annex/p10.tex': ('\\begin{annexitem}{annex:p10.two.1}{def:p10-two}x\\end{annexitem}\n'
                      '\\begin{annexitem}{annex:p10.x.1}{def:p09-a}x\\end{annexitem}\n'),
    'bib/handbook.bib': '@book{Src2020,\n  title={Fixture}\n}\n',
}
# Routed after the capture: a new P10 chapter between One and Two.
POST_CAPTURE = {
    'parts/p10.tex': '\\part{Ten}\\label{part:p10}\n\\input{parts/p10/one}\n\\input{parts/p10/new}\n\\input{parts/p10/two}\n',
    'parts/p10/new.tex': '\\chapter{New}\\label{sec:p10-new}\n\\begin{hbdefinition}{def:p10-new}x\\end{hbdefinition}\n',
}

FIXTURE_ROWS = [
    ['\\(a\\)', 'a', 'whole-chapter role', 'P9.1', 'n/a', 'P9.1', 'chapter row'],
    ['\\(a\\)', 'a', 'ghost role', 'P9.3', 'n/a', 'P9.3', 'ghost row, same glyph'],
    ['\\(b\\)', 'b_q', 'ghost role', 'P9.3', 'n/a', 'P9.3', 'second ghost row; used only in P9.2'],
    ['\\(c\\)', 'c', 'cross role', 'P9-P10', 'n/a', 'P9.2', 'whole parts'],
    ['\\(d\\)', 'd', 'broad role', 'P10', 'n/a', 'P10.1', 'whole part 10'],
    ['\\(e\\)', 'e', 'partial cross', 'P9.2-P10.1', 'n/a', 'P9.2', 'two parts, partial'],
    ['\\(f\\)', 'f', 'global role', 'global', 'n/a', 'P10.2', 'numeric first use only'],
    ['\\(g\\)', 'g', 'ghost evidence', 'P10.3', 'n/a', 'P10.3', 'P10 ordinal beyond sections'],
    ['\\(d\\)', 'd', 'local role', 'P10 local', 'n/a', 'def:p10-two', 'override row'],
    ['\\(q\\)', 'q', 'capture two role', 'P10.2', 'n/a', 'P10.2', 'live numbering now means New'],
    ['\\(q\\)', 'q', 'new chapter role', 'sec:p10-new', 'n/a', 'sec:p10-new', 'post-capture chapter row'],
]


def build_fixture(root):
    base = root / 'handbook'
    for rel, text in FIXTURE.items():
        (base / rel).parent.mkdir(parents=True, exist_ok=True)
        (base / rel).write_text(text, encoding='utf-8', newline='\n')
    lines = [','.join(reg.HEADER)] + [','.join(csv_field(c) for c in r) for r in FIXTURE_ROWS]
    (base / 'registry').mkdir()
    (base / 'registry/symbols.csv').write_text('\n'.join(lines) + '\n', encoding='utf-8', newline='\n')
    scopes = {'schema_version': 1, 'scopes': {'P10 local': {
        'presentation': 'fixture local scope', 'regions': [{'anchor': 'sec:p10-two'}],
        'overrides': [{'glyph': '\\(d\\)', 'local_role': 'local role', 'first_use': 'def:p10-two',
                       'broader_scope': 'P10', 'broader_role': 'broad role', 'reason': 'fixture', 'source': 'Src2020'}]}}}
    (base / 'registry/symbol-scopes.json').write_text(json.dumps(scopes, indent=2) + '\n', encoding='utf-8', newline='\n')
    # Capture in the baseline's shape (as prepare_oct3_batch5_intakes.capture_pre_route builds it).
    index = reg.ReaderIndex(base)
    chapters = []
    for h in index.heading_records:
        if h.kind == 'chapter' and h.chapter is not None:
            label = [d.label for sites in index.labels.values() for d in sites
                     if d.path == h.path and d.start == h.start and d.kind == 'chapter'][0]
            chapters.append({'part': h.part, 'chapter': h.chapter, 'path': h.path, 'line': h.line, 'start': h.start,
                             'end': h.end, 'selectors': [{'anchor': label}], 'valid_first_use': label})
    numeric = []
    for line, r in enumerate(FIXTURE_ROWS, 2):
        interval = numeric_scope(r[3])
        if interval:
            numeric.append({'canonical_line': line, 'original': dict(zip(reg.HEADER, r)), 'interval': list(interval),
                            'old_chapters': [c for c in chapters if interval[0] <= c['part'] * 1000 + c['chapter'] <= interval[1]]})
    baseline = root / 'baseline.json'
    baseline.write_text(json.dumps({'canonical_symbols_sha256': sha(base / 'registry/symbols.csv'),
                                    'canonical_scopes_sha256': sha(base / 'registry/symbol-scopes.json'),
                                    'chapters': chapters, 'numeric_rows': numeric}), encoding='utf-8', newline='\n')
    ghost = root / 'ghost.json'
    ghost.write_text(json.dumps({'9': {'scope': 'P10 two evidence', 'first_use': 'def:p10-two',
                                       'regions': [{'anchor': 'sec:p10-two'}]},
                                 '3': {'scope': 'sec:p09-c', 'first_use': 'sec:p09-c'}}), encoding='utf-8', newline='\n')
    for rel, text in POST_CAPTURE.items():
        (base / rel).write_text(text, encoding='utf-8', newline='\n')
    return base, baseline, ghost


def write_decisions(path, report, reading='own-file'):
    path.write_text(json.dumps({'ghost_reading': reading, 'accepted_collisions': report['decision_needed']}),
                    encoding='utf-8', newline='\n')
    return path


def selftest():
    assert raw_fields('"a,b",c,"d""e"') == ['"a,b"', 'c', '"d""e"']
    assert stem('sec:p09-description-logics') == 'description-logics' and stem('ch:set-prerequisites') == 'set-prerequisites'
    assert top_level_split('R_P(h,f),\\widehat R_S(h), m') == ['R_P(h,f)', '\\widehat R_S(h)', 'm']
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        base, baseline, ghost = build_fixture(root)
        csv_path, scopes_path = base / 'registry/symbols.csv', base / 'registry/symbol-scopes.json'
        csv_before, scopes_before = csv_path.read_bytes(), scopes_path.read_bytes()
        report, new_csv, new_json = migrate(base, baseline, ghost)
        b, names = report['bindings'], report['numeric_scope_bindings']
        assert report['rows_still_numeric'] == [] and report['read_rows_errors'] == [], report['read_rows_errors']
        assert report['scope_strings_with_more_than_one_binding'] == {}
        # Exact coverage everywhere: nothing narrowed, nothing widened.
        assert report['coverage']['differences'] == {}, report['coverage']['differences']
        # Whole chapter P9.1 = chapter plus its owned annex items, wherever they are hosted.
        # (Its P10-hosted item makes the regions two-part, so the name is spelt 'Part 9'.)
        assert names['P9.1'] == 'Part 9 mono', names
        assert report['diagnostics']['renamed_for_foreign_hosted_annex_items'] == ['Part 9 mono']
        p91 = b['Part 9 mono']['regions']
        assert {'anchor': 'sec:p09-mono'} in p91 and {'file': 'annex/p09/c.tex'} in p91 and {'anchor': 'annex:p9.a.1'} in p91
        assert {'anchor': 'annex:p10.x.1'} in p91 and {'anchor': 'annex:p9.s.1'} not in p91
        # Ghost P9.3 (own-file reading): starred and fragment sections skipped.
        assert names['P9.3'] == 'P9 legacy unit 3 c', names
        assert b['P9 legacy unit 3 c']['regions'] == [{'anchor': 'sec:p09-c'}, {'file': 'annex/p09/c.tex'}]
        rows = {r['line']: r for r in report['rows_rebound']}
        assert rows[3]['scope'][1] == rows[4]['scope'][1] == 'P9 legacy unit 3 c' and rows[3]['first_use'][1] == 'sec:p09-c'
        agreement = report['ghost_reading_agreement']['ordinals']['P9.3']
        assert agreement['own-file'] == {'unit': 'sec:p09-c', 'agrees': True}
        assert agreement['route-order'] == {'unit': 'sec:p09-fragment', 'agrees': False}
        # Whole parts: driver files, except a file holding something outside the meaning
        # (the post-capture chapter New; the foreign-owned annex:p10.x.1 for P10 alone).
        assert names['P9-P10'] == 'Parts 9\u201310 from mono'
        cross = b['Parts 9\u201310 from mono']['regions']
        assert {'file': 'parts/p09.tex'} in cross and {'file': 'annex/p10.tex'} in cross
        assert {'file': 'parts/p10.tex'} not in cross and {'file': 'parts/p10/new.tex'} not in cross
        assert {'file': 'parts/p10/one.tex'} in cross and {'file': 'parts/p10/two.tex'} in cross
        assert names['P10'] == 'P10 one to two' and rows[6]['first_use'][1] == 'sec:p10-one'
        p10 = b['P10 one to two']['regions']
        assert {'file': 'annex/p10.tex'} not in p10 and {'anchor': 'annex:p10.two.1'} in p10 and {'anchor': 'annex:p10.x.1'} not in p10
        assert names['P9.2-P10.1'] == 'Parts 9\u201310 from second to one'
        assert rows[8]['scope'][1] == 'global' and rows[8]['first_use'][1] == 'sec:p10-two'
        # P10.2 keeps its capture meaning (Two), although live numbering now means New.
        assert names['P10.2'] == 'P10 two' and rows[11]['first_use'][1] == 'sec:p10-two'
        # P10 ordinal beyond the chapter's sections: ghost-map evidence.
        assert names['P10.3'] == 'P10 legacy unit 3 two'
        assert b['P10 legacy unit 3 two']['regions'] == [{'anchor': 'sec:p10-two'}, {'anchor': 'annex:p10.two.1'}]
        # Override broader_scope rewritten to the same binding as its numeric string.
        assert report['override_rewrites'] == [{'scope': 'P10 local', 'glyph': '\\(d\\)', 'first_use': 'def:p10-two',
                                                'broader_scope': ['P10', 'P10 one to two']}]
        assert json.loads(new_json)['scopes']['P10 local']['overrides'][0]['broader_scope'] == 'P10 one to two'
        # Baseline collisions use capture identities: the live-only q collision (P10.2 = New
        # in live numbering) is not part of it, and the ghost rebinding's new a overlap is listed.
        cc = report['collision_check']
        assert any(e.startswith('lines 11/12:') for e in reg.collision_check(reg.read_rows(csv_path, base=base)[0]))
        assert not any(e.startswith('lines 11/12:') for e in cc['capture_meaning'] + cc['migrated'])
        assert len(report['decision_needed']) == 1 and report['decision_needed'][0].startswith('lines 2/3:'), report['decision_needed']
        assert report['post_capture_chapters'] == ['parts/p10/new.tex:1']
        # Usage signal: b_q is used only in P9.2, outside 'P9 legacy unit 3 c'.
        assert [(m['line'], m['tokens_used_only_outside_binding']) for m in report['usage_meaning_mismatches']] == \
            [(4, {'b_q': ['parts/p09/second.tex']})]
        # In-place edit: same line count, only scope/first_use cells changed.
        old_lines, new_lines = csv_before.decode().split('\n'), new_csv.split('\n')
        assert len(old_lines) == len(new_lines)
        for o, n in zip(old_lines[1:], new_lines[1:]):
            if o:
                oc, nc = next(csv.reader([o])), next(csv.reader([n]))
                assert [oc[i] for i in (0, 1, 2, 4, 6)] == [nc[i] for i in (0, 1, 2, 4, 6)]
        # The literal route-order reading binds P9.3 to the fragment section.
        alt = migrate(base, baseline, ghost, 'route-order')[0]
        assert alt['numeric_scope_bindings']['P9.3'] == 'P9 legacy unit 3 fragment'
        # Dry run writes only the report and exits 1 while decisions are open.
        out = root / 'out/dry-run.json'
        assert run(base, baseline, ghost, out, apply=False) == 1
        assert out.is_file() and csv_path.read_bytes() == csv_before and scopes_path.read_bytes() == scopes_before
        # --apply refuses without recorded decisions, and with collisions not all accepted.
        assert run(base, baseline, ghost, out, apply=True) == 1 and csv_path.read_bytes() == csv_before
        partial = root / 'partial.json'
        partial.write_text(json.dumps({'ghost_reading': 'own-file'}), encoding='utf-8', newline='\n')
        assert run(base, baseline, ghost, out, apply=True, decisions_path=partial) == 1 and csv_path.read_bytes() == csv_before
        # Staged writes re-check the hashes: a concurrent edit refuses and leaves both files intact.
        target = root / 'pair'
        target.mkdir()
        (target / 'x.txt').write_text('x\n', encoding='utf-8', newline='\n')
        (target / 'y.txt').write_text('y\n', encoding='utf-8', newline='\n')
        try:
            write_files([(target / 'x.txt', 'X\n'), (target / 'y.txt', 'Y\n')],
                        {target / 'x.txt': sha(target / 'x.txt'), target / 'y.txt': 'stale'})
            raise AssertionError('changed file not refused')
        except Refusal:
            pass
        assert sorted(p.name for p in target.iterdir()) == ['x.txt', 'y.txt'] and (target / 'x.txt').read_text() == 'x\n'
        # With every decision recorded, --apply writes both files: LF, no BOM.
        decisions = write_decisions(root / 'decisions.json', report)
        assert run(base, baseline, ghost, out, apply=True, decisions_path=decisions) == 0
        applied = csv_path.read_bytes()
        assert applied == new_csv.encode('utf-8') and b'\r' not in applied and not applied.startswith(b'\xef\xbb\xbf')
        assert scopes_path.read_text(encoding='utf-8') == new_json
        # Hash mismatch: refuse with exit 1 and write nothing, dry run included.
        out2 = root / 'out2/dry-run.json'
        assert run(base, baseline, ghost, out2, apply=False) == 1 and not out2.exists()
        assert csv_path.read_bytes() == applied
        for broken in ('symbols.csv', 'symbol-scopes.json'):
            try:
                migrate(base, baseline, ghost)
                raise AssertionError('hash mismatch not refused')
            except Refusal as exc:
                assert f'sha256({broken})' in str(exc)
            csv_path.write_bytes(csv_before)
    # Narrowing: a second annexitem reusing annex:p9.c.1 cannot be anchored, so 'P9 mono'
    # would lose both sites. The migration must report it and --apply must refuse.
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        base, baseline, ghost = build_fixture(root)
        csv_before = (base / 'registry/symbols.csv').read_bytes()
        with open(base / 'annex/p09/c.tex', 'a', encoding='utf-8', newline='\n') as stream:
            stream.write('\\begin{annexitem}{annex:p9.c.1}{thm:p09-c}y\\end{annexitem}\n')
        report = migrate(base, baseline, ghost)[0]
        assert 'Part 9 mono' in report['coverage']['bindings_narrowed'], report['coverage']
        assert any(m.startswith('annex:p9.c.1') for m in report['coverage']['differences']['Part 9 mono']['missing'])
        decisions = write_decisions(root / 'decisions.json', report)
        assert run(base, baseline, ghost, root / 'out.json', apply=True, decisions_path=decisions) == 1
        assert (base / 'registry/symbols.csv').read_bytes() == csv_before
    print('selftest ok')
    return 0


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--apply', action='store_true', help='write symbols.csv and symbol-scopes.json (default: dry run)')
    ap.add_argument('--decisions', type=Path, help='JSON recording the ghost reading and accepted collisions')
    ap.add_argument('--selftest', action='store_true', help='run fixture checks; touches no repository file')
    args = ap.parse_args(argv)
    if args.selftest:
        return selftest()
    return run(BASE, BASELINE, GHOST_MAP, OUT, args.apply, args.decisions)


if __name__ == '__main__':
    sys.exit(main())
