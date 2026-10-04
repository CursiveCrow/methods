"""Prepare a non-destructive append for the two already routed chapter intakes."""
from pathlib import Path
from datetime import datetime,timezone
import csv,hashlib,io,json,re,sys
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'tools'))
import check as grammar
target=ROOT/'handbook/registry/symbols.csv'
source=ROOT/'handbook/registry/symbols-intake-p17-19-p19-11-integration.csv'
old=target.read_text(encoding='utf-8-sig');incoming=source.read_text(encoding='utf-8-sig')
existing=list(csv.DictReader(io.StringIO(old)));new=list(csv.DictReader(io.StringIO(incoming)))
fields=['glyph','macro','role','scope','precedence','first_use','notes']
assert len(new)==34 and list(new[0])==fields
assert all(set(r)==set(fields) and all(r[k] for k in fields) for r in new)
known={tuple(r[k] for k in fields) for r in existing}
assert all(tuple(r[k] for k in fields) not in known for r in new),'Intake already partly/fully merged; inspect before append'
labels=set()
for rel in ['handbook/parts/p17/epistemic-nash-conditions.tex','handbook/annex/p17/epistemic-nash-conditions.tex','handbook/parts/p19/explanatory-preferences.tex','handbook/annex/p19/explanatory-preferences.tex']:
    text=grammar.strip_verbatims(grammar.strip_comments((ROOT/rel).read_text(encoding='utf-8-sig')))
    labels.update(re.findall(r'\\label\{([^{}]+)\}',text))
    for m in grammar.HB_ENV_RE.finditer(text):
        args,_=grammar.scan_braced_args(text,m.end(),1)
        if args:labels.add(args[0])
missing=sorted({r['first_use'] for r in new}-labels)
assert not missing,missing
last=old.rstrip('\r\n').splitlines()[-1]
rawrows=incoming.splitlines()[1:]
assert len([r for r in rawrows if r.strip()])==34
patch='*** Begin Patch\n*** Update File: '+target.as_posix()+'\n@@\n '+last+'\n'+'\n'.join('+'+r for r in rawrows)+'\n*** End Patch'
bib=(ROOT/'handbook/bib/handbook.bib').read_text(encoding='utf-8-sig')
keys=['AumannBrandenburger1995Epistemic','Lombrozo2007SimplicityProbability']
assert all(len(re.findall(r'@\w+\{'+key+r'\s*,',bib))==1 for key in keys)
receipt=dict(date_utc=datetime.now(timezone.utc).isoformat(),symbol_rows=34,scopes=['P17.19','P19.11'],all_first_use_labels_declared=True,bibliography_keys=keys,each_bibliography_key_once=True,source_intake_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),symbols_before_sha256=hashlib.sha256(target.read_bytes()).hexdigest(),source_intake_preserved=True,scope='Canonical integration of already routed treatments. Independent content/production acceptance remains pending.')
print(json.dumps(dict(patch=patch,receipt=receipt),ensure_ascii=False))
