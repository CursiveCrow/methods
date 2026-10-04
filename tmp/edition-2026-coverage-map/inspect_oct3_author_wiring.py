"""Read-only integration checks; never mathematical/source admission."""
from pathlib import Path
import csv
import hashlib
import json
import re
import sys
import argparse

root = Path(r'C:\Dev\the-methods-of-reason')
base = root / 'handbook'
sys.path.insert(0, str(root / 'tools'))
import check as grammar
import symbol_registry as registry

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--manifest', default='spec/research/edition-2026-authoring-batch-intake-3.json')
args = parser.parse_args()
manifest = json.loads((root / args.manifest).read_text(encoding='utf-8'))
groups = list(manifest['groups'])
if args.manifest.endswith('edition-2026-authoring-batch-intake-3.json'):
    groups += [
    {'stem': 'p07-girard-empires', 'bodies': ['parts/p07/girard-1987-trips-and-empires.tex'], 'annex': 'annex/p07/girard-1987-trips-and-empires.tex'},
    {'stem': 'p10-domain-invariance', 'bodies': ['parts/p10/domain-recursion-and-invariance.tex'], 'annex': 'annex/p10/domain-recursion-and-invariance.tex'}]
index = registry.ReaderIndex(base)
labels = set(index.labels)
dynamic_sheets = set()
for rel in index.files:
    path = base / rel
    if not path.is_file():
        continue
    text = grammar.strip_comments(path.read_text(encoding='utf-8-sig'))
    for slug in re.findall(r'\\showcalculus\s*\{([^{}]+)\}', text):
        sheet = base / 'registry/calculi' / (slug + '.tex')
        if not sheet.is_file():
            raise RuntimeError('Missing literal calculus input ' + str(sheet))
        dynamic_sheets.add(sheet.relative_to(base).as_posix())
        sheet_text = grammar.strip_comments(sheet.read_text(encoding='utf-8-sig'))
        labels.update(re.findall(r'\\(?:calculussheet|hbrule)\s*\{([^{}]+)\}', sheet_text))
rows, row_errors = registry.read_rows(base / 'registry/symbols.csv', base=base)
bib = (base / 'bib/handbook.bib').read_text(encoding='utf-8-sig')
keys = re.findall(r'@\w+\s*\{\s*([^,\s{}]+)', bib)
errors = list(index.errors) + row_errors + registry.collision_check(rows)
if len(keys) != len(set(keys)):
    errors.append('duplicate canonical bibliography keys')
results = []
for group in groups:
    body_records = {}
    annex_records = {}
    paths = group['bodies'] + group.get('annexes', ([group['annex']] if group.get('annex') else []))
    pins = []
    for rel in paths:
        path = base / rel
        if len(index.files.get(rel, [])) != 1:
            errors.append(f'route count {rel}: {len(index.files.get(rel, []))}')
        text = grammar.strip_verbatims(grammar.strip_comments(path.read_text(encoding='utf-8-sig')))
        pins.append({'path': 'handbook/' + rel, 'sha256': hashlib.sha256(path.read_bytes()).hexdigest()})
        for match in grammar.HB_ENV_RE.finditer(text):
            if match.group(1) not in grammar.HB_STATUS_ENVS and match.group(1) != 'annexitem':
                continue
            args, _ = grammar.scan_braced_args(text, match.end(), 3)
            if len(args) != 3:
                errors.append(f'malformed result {rel}')
                continue
            target = annex_records if match.group(1) == 'annexitem' else body_records
            if args[0] in target:
                errors.append('duplicate incoming result ' + args[0])
            target[args[0]] = args
        for match in re.finditer(r'\\(?:ref|cref|Cref|eqref|pageref|autoref)\s*\{([^{}]+)\}|\\hyperref\[([^]]+)\]', text):
            for label in (match.group(1) or match.group(2)).split(','):
                if label.strip() not in labels:
                    errors.append(f'unresolved incoming reference {rel}: {label.strip()}')
        for match in re.finditer(r'\\(?:cite|parencite|textcite|autocite)(?:\[[^]]*\])*\s*\{([^{}]+)\}', text):
            for key in match.group(1).split(','):
                if key.strip() not in keys:
                    errors.append(f'unresolved incoming citation {rel}: {key.strip()}')
    proved = {k: v for k, v in body_records.items() if v[1].startswith('proved=')}
    for key, args in proved.items():
        target = args[1].split('=', 1)[1]
        if target not in annex_records or annex_records[target][1] != key:
            errors.append('incoming reciprocal mismatch ' + key)
    for key, args in annex_records.items():
        if args[1] not in proved or proved[args[1]][1] != 'proved=' + key:
            errors.append('incoming reverse mismatch ' + key)
    results.append({'stem': group['stem'], 'proved_pairs': len(proved), 'annex_items': len(annex_records), 'pins': pins})
print(json.dumps({'standing': 'Incoming route/reference/citation/typed-row/reciprocal checks only; no proof or source acceptance',
                  'groups': results, 'canonical_symbol_rows': len(rows), 'canonical_bib_keys': len(keys),
                  'literal_dynamic_calculus_files': len(dynamic_sheets),
                  'errors': errors}, ensure_ascii=False))
