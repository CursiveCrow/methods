"""Recover the completed repair receipt after its first write was denied."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,re,sys
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/"tools"))
import check as grammar
base={u['destination']['annex']['path']:u['destination']['annex'].get('sha256') for u in [json.loads(l) for l in (ROOT/'spec/coverage/edition-2026/current-reasoning-units.jsonl').read_text(encoding='utf-8').splitlines()] if u.get('destination',{}).get('annex',{}).get('exists')}
targets=[('p15','huber-information-game'),('p15','huber-joint-endpoints'),('p15','huber-remaining-methods'),('p19','mental-rotation-and-spatial-reasoning')]
records=[]
for part,slug in targets:
    relative=f'handbook/annex/{part}/{slug}.tex';path=ROOT/relative
    text=path.read_text(encoding='utf-8-sig');assert 'hbproof' not in text
    result=[];tail=0;blocks=[]
    for m in re.finditer(r'\\begin\{annexitem\}',text):
        args,end=grammar.scan_braced_args(text,m.end(),3);assert len(args)==3
        assert text.startswith('\n\\begin{proof}',end)
        payload_start=end+len('\n\\begin{proof}')
        close=text.index('\\end{proof}\n\\end{annexitem}',payload_start)
        payload=text[payload_start:close]
        result += [text[tail:m.start()],r'\begin{hbproof}{'+args[0]+'}{'+args[1]+'}'+payload+r'\end{hbproof}']
        tail=close+len('\\end{proof}\n\\end{annexitem}')
        blocks.append(dict(annex_label=args[0],body_label=args[1],title=args[2],payload_sha256=hashlib.sha256(payload.encode()).hexdigest()))
    result.append(text[tail:]);original=''.join(result)
    candidates=[original.encode(),original.replace('\n','\r\n').encode()]
    candidates += [b'\xef\xbb\xbf'+s for s in list(candidates)]
    assert base[relative].lower() in {hashlib.sha256(s).hexdigest() for s in candidates},relative
    body=(ROOT/f'handbook/parts/{part}/{slug}.tex').read_text(encoding='utf-8-sig')
    for b in blocks:
        assert f"{{{b['body_label']}}}{{proved={b['annex_label']}}}" in body,b
    records.append(dict(annex_path=relative,body_path=f'handbook/parts/{part}/{slug}.tex',before_sha256=base[relative],after_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),all_original_proof_payloads_preserved=True,reciprocal_entries=blocks))
assert sum(len(r['reciprocal_entries']) for r in records)==39
print(json.dumps(dict(date_utc=datetime.now(timezone.utc).isoformat(),files=records,entries=39,scope='Mechanical integration repair only. Reconstructing the prior wrappers recovers the pinned pre-edit file hash; original proof text and targets are preserved. No independent mathematical acceptance inferred.',consolidated_production_checks='pending the complete writing/integration batch'),ensure_ascii=False))
