"""Prepare an append-only intake patch after a writer's actual files are routed.

This helper reads and checks; the lead applies its emitted patch. It makes no
source acceptance or proof-correctness decision and never edits a baseline.
"""
import argparse
import csv
import hashlib
import io
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'tools'))
import check as grammar
import symbol_registry as registry

ap = argparse.ArgumentParser()
ap.add_argument('--stem', required=True)
ap.add_argument('--body', required=True)
ap.add_argument('--annex', required=True)
ap.add_argument('--no-bib', action='store_true')
ap.add_argument('--external-body', action='append', default=[])
args = ap.parse_args()
base = ROOT / 'handbook'
source_files = []
entries = {}
index = registry.ReaderIndex(base)
for mode, relative in [('body', args.body), ('annex', args.annex)]:
    path = base / relative
    assert len(index.files.get(relative, [])) == 1, ('reader route', relative)
    text = grammar.strip_verbatims(grammar.strip_comments(path.read_text(encoding='utf-8-sig')))
    records = {}
    for match in grammar.HB_ENV_RE.finditer(text):
        env = match.group(1)
        if env not in grammar.HB_STATUS_ENVS and env != 'annexitem':
            continue
        fields, _ = grammar.scan_braced_args(text, match.end(), 3)
        assert len(fields) == 3, (relative, match.start())
        assert fields[0] not in records, fields[0]
        records[fields[0]] = fields
    entries[mode] = records
    source_files.append({'path': path.relative_to(ROOT).as_posix(), 'sha256': hashlib.sha256(path.read_bytes()).hexdigest()})
needed = {a[1] for a in entries['annex'].values()} - set(entries['body'])
for relative in args.external_body:
    path = base / relative
    assert len(index.files.get(relative, [])) == 1, ('external reader route', relative)
    text = grammar.strip_verbatims(grammar.strip_comments(path.read_text(encoding='utf-8-sig')))
    for match in grammar.HB_ENV_RE.finditer(text):
        if match.group(1) not in grammar.HB_STATUS_ENVS:
            continue
        fields, _ = grammar.scan_braced_args(text, match.end(), 3)
        if len(fields) == 3 and fields[0] in needed:
            assert fields[0] not in entries['body'], fields[0]
            entries['body'][fields[0]] = fields
    source_files.append({'path': path.relative_to(ROOT).as_posix(), 'sha256': hashlib.sha256(path.read_bytes()).hexdigest(), 'role': 'existing body targets for this annex'})
proved = {k: a for k, a in entries['body'].items() if a[1].startswith('proved=')}
for key, fields in proved.items():
    assert entries['annex'][fields[1].split('=', 1)[1]][1] == key, key
assert len(entries['annex']) == len(proved), 'annex count differs'

symbol = base / 'registry/symbols.csv'
intake = base / f'registry/symbols-intake-{args.stem}.csv'
symbol_text = symbol.read_text(encoding='utf-8-sig')
intake_text = intake.read_text(encoding='utf-8-sig')
old_rows = list(csv.DictReader(io.StringIO(symbol_text)))
new_rows = list(csv.DictReader(io.StringIO(intake_text)))
assert all(row not in old_rows for row in new_rows), 'intake already merged'
parsed_old, errors = registry.read_rows(symbol, base=base)
parsed_new, new_errors = registry.read_rows(intake, base=base)
assert not errors + new_errors, errors + new_errors
collisions = registry.collision_check(parsed_old + parsed_new)
assert not collisions, collisions
patches = ['*** Begin Patch\n*** Update File: ' + symbol.as_posix() + '\n@@\n '
           + symbol_text.rstrip().splitlines()[-1] + '\n'
           + '\n'.join('+' + line for line in intake_text.splitlines()[1:] if line.strip())
           + '\n*** End Patch']
keys = []
if not args.no_bib:
    bib = base / 'bib/handbook.bib'
    bib_text = bib.read_text(encoding='utf-8-sig')
    bib_intake = base / f'bib/intake-{args.stem}.bib'
    new_bib = bib_intake.read_text(encoding='utf-8-sig')
    keys = re.findall(r'@\w+\s*\{\s*([^,\s{}]+)', new_bib)
    old_keys = re.findall(r'@\w+\s*\{\s*([^,\s{}]+)', bib_text)
    assert len(keys) == len(set(keys)) and not set(keys).intersection(old_keys), keys
    last = list(re.finditer(r'@\w+\s*\{', bib_text))[-1]
    _, end = grammar.scan_braced_args(bib_text, last.end() - 1, 1)
    patches.append('*** Begin Patch\n*** Update File: ' + bib.as_posix() + '\n@@\n'
                   + '\n'.join(' ' + line for line in bib_text[last.start():end].splitlines())
                   + '\n+\n' + '\n'.join('+' + line for line in new_bib.splitlines())
                   + '\n*** End Patch')
print(json.dumps({'patches': patches, 'receipt': {
    'stem': args.stem, 'source_files': source_files, 'proved_pairs': len(proved),
    'symbol_intake': intake.relative_to(ROOT).as_posix(),
    'symbol_intake_sha256': hashlib.sha256(intake.read_bytes()).hexdigest(),
    'new_symbol_rows': len(new_rows), 'canonical_rows_after': len(old_rows) + len(new_rows),
    'new_bibliography_keys': keys,
    'standing': 'Author-return integration; source, mathematical and publication acceptance remain separate.'}}))
