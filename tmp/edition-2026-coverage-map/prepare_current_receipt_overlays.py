"""Prepare small current-qualification patches; preserve historical receipts."""
from collections import Counter
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path

root = Path(r'C:\Dev\the-methods-of-reason')
folder = root / 'spec/coverage/edition-2026/current-fulfillment'
results = []
for ledger in sorted(folder.glob('*.jsonl')):
    receipt = ledger.with_name(ledger.stem + '-receipt.json')
    text = receipt.read_text(encoding='utf-8-sig')
    key = '"reader_adoption_current_qualification"'
    at = text.index(key)
    start = text.rfind('\n', 0, at) + 1
    value = text.index(':', at) + 1
    while text[value].isspace():
        value += 1
    _, extent = json.JSONDecoder().raw_decode(text[value:])
    end = value + extent
    suffix = ',' if text[end:end+1] == ',' else ''
    old = text[start:end+len(suffix)]
    rows = [json.loads(line) for line in ledger.read_text(encoding='utf-8-sig').splitlines() if line.strip()]
    new_value = {
        'observed_utc': datetime.now(timezone.utc).isoformat(),
        'ledger_path': ledger.relative_to(root).as_posix(),
        'ledger_sha256': hashlib.sha256(ledger.read_bytes()).hexdigest(),
        'rows': len(rows),
        'unique_ids': len({row['section_id'] for row in rows}),
        'status_counts': dict(Counter(row['status'] for row in rows)),
        'standing': 'Current saved section-writing qualification after 59 targeted actual-reader reconciliations. Original source facets and historical receipt payloads remain preserved. Later batch5 and follow-on writing is not automatically reclassified; no independent correctness/source admission or publication acceptance.'
    }
    new = '  ' + key + ': ' + json.dumps(new_value, ensure_ascii=False, indent=2).replace('\n', '\n  ') + suffix
    patch = ('*** Begin Patch\n*** Update File: ' + receipt.as_posix() + '\n@@\n' +
             '\n'.join('-'+line for line in old.splitlines()) + '\n' +
             '\n'.join('+'+line for line in new.splitlines()) + '\n*** End Patch\n')
    results.append({'receipt': receipt.relative_to(root).as_posix(), 'patch_text': patch})
assert len(results) == 9
print(json.dumps(results, ensure_ascii=False))
