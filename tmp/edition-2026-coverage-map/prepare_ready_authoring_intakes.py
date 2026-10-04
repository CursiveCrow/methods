"""Prepare canonical intake append for the completed first author returns."""
from pathlib import Path
import csv,hashlib,io,json,re,sys
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'tools'))
import check as grammar
groups=[
 ('p08','modal-canonical-extensions','p08-modal-canonical-extensions',None),
 ('p12','small-clause-standard','p12-small-clause-standard',None),
 ('p12','small-clause-optimizations','p12-small-clause-optimizations','p12-small-clause-optimizations'),
 ('p02','syllogistic-inference','p02-syllogistic','p02-syllogistic'),
 ('p17','judgment-aggregation','p17-judgment-aggregation','p17-judgment-aggregation'),
 ('p15','posterior-predictive-model-criticism','p15-posterior-predictive','p15-posterior-predictive'),
 ('p18','question-evocation','p18-question-evocation','p18-question-evocation'),
 ('p15','measurement-uncertainty','p15-measurement-uncertainty','p15-measurement-uncertainty'),
 ('p03','presentations/fraisse-1954','p03-fraisse-1954','p03-fraisse-1954'),
 ('p12','numerical-error-and-inference','p12-numerical-error','p12-numerical-error')]
def bibrecords(text):
    out={}
    for m in re.finditer(r'@\w+\s*\{',text):
        a,end=grammar.scan_braced_args(text,m.end()-1,1)
        if a and ',' in a[0]:
            key=a[0].split(',',1)[0].strip();assert key not in out,key
            out[key]=text[m.start():end]
    return out
fields=['glyph','macro','role','scope','precedence','first_use','notes']
symbol_path=ROOT/'handbook/registry/symbols.csv';symbol_text=symbol_path.read_text(encoding='utf-8-sig')
existing={tuple(r[k] for k in fields) for r in csv.DictReader(io.StringIO(symbol_text))}
bib_path=ROOT/'handbook/bib/handbook.bib';bib_text=bib_path.read_text(encoding='utf-8-sig');known_bibs=bibrecords(bib_text)
labels=set();sources=[];pairs=[]
for part,slug,_,_ in groups:
    parsed={}
    for mode in ['parts','annex']:
        path=ROOT/f'handbook/{mode}/{part}/{slug if mode=="parts" else slug.rsplit("/",1)[-1]}.tex'
        text=grammar.strip_verbatims(grammar.strip_comments(path.read_text(encoding='utf-8-sig')))
        labels.update(re.findall(r'\\label\{([^{}]+)\}',text))
        entries={}
        for m in grammar.HB_ENV_RE.finditer(text):
            env=m.group(1);arity=3 if env in grammar.HB_STATUS_ENVS or env=='annexitem' else 2
            args,end=grammar.scan_braced_args(text,m.end(),arity)
            if len(args)==arity:
                labels.add(args[0])
                if env in grammar.HB_STATUS_ENVS or env=='annexitem':
                    assert args[0] not in entries,args[0]
                    entries[args[0]]=args
        parsed[mode]=entries
        sources.append(dict(path=path.relative_to(ROOT).as_posix(),sha256=hashlib.sha256(path.read_bytes()).hexdigest()))
    proofs={key:args for key,args in parsed['parts'].items() if args[1].startswith('proved=')}
    for key,args in proofs.items():
        target=args[1].split('=',1)[1]
        assert target in parsed['annex'],target
        assert parsed['annex'][target][1]==key,key
    assert len(parsed['annex'])==len(proofs),(slug,len(parsed['annex']),len(proofs))
    pairs.append(dict(part=part,slug=slug,proved_pairs=len(proofs)))
assert sum(p['proved_pairs'] for p in pairs)==120
new_symbols=[];new_bibs={};intakes=[];existing_bib_intakes=[]
for part,slug,symbol_stem,bib_stem in groups:
    p=ROOT/f'handbook/registry/symbols-intake-{symbol_stem}.csv'
    text=p.read_text(encoding='utf-8-sig');data=list(csv.DictReader(io.StringIO(text)))
    assert data and list(data[0])==fields,p
    for row in data:
        assert set(row)==set(fields) and all(row[k] for k in fields),row
        assert row['first_use'] in labels,row
        sig=tuple(row[k] for k in fields)
        assert sig not in existing,'Intake already merged: '+str(p)
        existing.add(sig);new_symbols.append(row)
    intakes.append(dict(path=p.relative_to(ROOT).as_posix(),sha256=hashlib.sha256(p.read_bytes()).hexdigest(),rows=len(data)))
    if bib_stem:
        p=ROOT/f'handbook/bib/intake-{bib_stem}.bib'
        records=bibrecords(p.read_text(encoding='utf-8-sig'))
        for key,value in records.items():
            if key=='Fraisse1954' and key in known_bibs:
                existing_bib_intakes.append(dict(key=key,canonical=known_bibs[key],intake=value,standing='Same original source; root will compare and apply metadata enrichment separately.'))
                continue
            assert key not in known_bibs and key not in new_bibs,'Existing bibliography key: '+key
            new_bibs[key]=value
        intakes.append(dict(path=p.relative_to(ROOT).as_posix(),sha256=hashlib.sha256(p.read_bytes()).hexdigest(),keys=list(records)))
assert len(new_symbols)==210,len(new_symbols)
buf=io.StringIO(newline='');writer=csv.DictWriter(buf,fieldnames=fields,lineterminator='\n',quoting=csv.QUOTE_ALL)
writer.writerows(new_symbols)
last=symbol_text.rstrip('\r\n').splitlines()[-1]
patch='*** Begin Patch\n*** Update File: '+symbol_path.as_posix()+'\n@@\n '+last+'\n'+'\n'.join('+'+line for line in buf.getvalue().splitlines())+'\n'
last_bib=list(known_bibs.values())[-1]
patch+='*** Update File: '+bib_path.as_posix()+'\n@@\n'+'\n'.join(' '+line for line in last_bib.splitlines())+'\n+\n'+'\n'.join('+'+line for line in '\n\n'.join(new_bibs.values()).splitlines())+'\n*** End Patch'
print(json.dumps(dict(patch=patch,receipt=dict(groups=pairs,source_files=sources,intakes=intakes,new_symbol_rows=len(new_symbols),new_bibliography_keys=list(new_bibs),existing_bibliography_intakes=existing_bib_intakes,proof_pairs=120,all_first_uses_declared=True,intakes_preserved=True,standing='Author-return structural integration only; separate source reproduction and independent acceptance remain open.')),ensure_ascii=False))
