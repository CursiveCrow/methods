"""Read and validate the fixed 59-row writing proposal; emit patches only."""
import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(r'C:\Dev\the-methods-of-reason')
WORK = ROOT / 'tmp/edition-2026-coverage-map/oct3-fulfillment-proposals'
LEDGERS = ROOT / 'spec/coverage/edition-2026/current-fulfillment'
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--row')
args = parser.parse_args()
manifest = json.loads((WORK / 'active-manifest.json').read_text(encoding='utf-8-sig'))
data = json.loads((WORK / 'proposals.json').read_text(encoding='utf-8-sig'))
assert manifest['final_pins'] and data['final_pins']
assert len(data['proposals']) == 59
assert set(manifest['proposal_sections']) == {p['section_id'] for p in data['proposals']}
allowed = {'status','reader_evidence','missing_pieces','unassessed_scope','reader_adoption_qualification','observed_utc'}
immutable = {'part','chapter_id','chapter_title','section_id','section_title','source_facets'}
selected = [p for p in data['proposals'] if args.row is None or p['section_id'] == args.row]
assert selected
result = []
for proposal in selected:
    shard = proposal['shard']
    assert shard.endswith('.jsonl') and Path(shard).name == shard
    target = LEDGERS / shard
    lines = target.read_text(encoding='utf-8-sig').splitlines()
    raw = lines[proposal['ledger_line'] - 1]
    current = json.loads(raw)
    assert hashlib.sha256(raw.encode()).hexdigest() == proposal['original_row_sha256'], proposal['section_id']
    assert current == proposal['before']
    after = proposal['after']
    assert all(current.get(k) == after.get(k) for k in immutable)
    assert {k for k in current.keys() | after.keys() if current.get(k) != after.get(k)} <= allowed
    assert after['status'] == 'partial'
    assert not after['reader_adoption_qualification']['whole_source_discharge']
    old_evidence = current.get('reader_evidence', [])
    assert after['reader_evidence'][:len(old_evidence)] == old_evidence
    for evidence in after['reader_evidence'][len(old_evidence):]:
        source = ROOT / evidence['path']
        assert source.is_file()
        assert hashlib.sha256(source.read_bytes()).hexdigest() == evidence['sha256'], evidence['path']
    serialized = json.dumps(after, ensure_ascii=False, separators=(',', ':'))
    patch = ('*** Begin Patch\n*** Update File: ' + target.as_posix() +
             '\n@@\n-' + raw + '\n+' + serialized + '\n*** End Patch\n')
    result.append({'section':proposal['section_id'],'target':target.as_posix(),
                   'old_status':current['status'],'new_status':after['status'],
                   'source_facets_preserved':len(after['source_facets']),
                   'patch_text':patch})
if args.row:
    print(json.dumps(result[0], ensure_ascii=False))
else:
    print(json.dumps({'rows':len(result),'sections':[r['section'] for r in result],
                      'transitions':{s:sum(r['old_status']==s for r in result)
                                     for s in ['missing','unassessed','partial']},
                      'source_facets_preserved':sum(r['source_facets_preserved'] for r in result),
                      'standing':'Actual writing qualifications only; no ledger writes or independent acceptance.'}, ensure_ascii=False))
