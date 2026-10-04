"""Read-only incoming routing/reference/intake check, not a content review."""
import collections
import hashlib
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'tools'))
import check
import symbol_registry as sr

B = ROOT / 'handbook'
groups = [
 ('p01-equivalence-closure','p01/equivalence-closure-and-quotients',4),
 ('p01-bpi-ultrafilters','p01/boolean-prime-ideal-and-ultrafilters',7),
 ('p06-proper-forcing-master','p06/proper-forcing-and-master-conditions',9),
 ('p09-timed-regions-zones','p09/timed-automata-regions-and-zones',9),
 ('p15-hume-induction','p15/hume-and-the-problem-of-induction',0),
 ('p07-ch88-ordinary-checking','p07/presentations/coquand-huet-1988-ordinary-checking',7),
 ('p07-ch88-object-product','p07/presentations/coquand-huet-1988-object-product',6),
 ('p12-equational-basic-completeness','p12/presentations/n-c-035-05-basic-completeness',5),
 ('p12-har-autarkic','p12/presentations/har2001-c18-autarkic',6),
 ('p12-har-kprime','p12/presentations/har2001-c18-kprime',8),
 ('p12-har-polynomial-normalizer','p12/presentations/har2001-c18-polynomial-normalizer',10),
 ('p15-fisher-estimation','p15/fisher-estimation-and-regularity',5),
 ('p15-rissanen-mdl','p15/rissanen-structural-and-numerical-inference',7),
 ('p16-nonmonotonic-causal-theories','p16/nonmonotonic-causal-theories',10),
 ('p09-negative-premises','p09/negative-premises-and-stratification',7),
 ('p15-probability-quantifiers','p15/probability-quantifiers',3),
 ('p16-peirce-abduction','p16/peirce-abduction-and-inquiry',0),
 ('p15-whewell-mill','p15/whewell-mill-scientific-induction',2),
 ('p15-goodman-projectibility','p15/goodman-projectibility',3),
 ('p15-fisher-grouping','p15/fisher-grouping-and-moments',6),
 ('p12-har-primitive-recursive-compiler','p12/presentations/har2001-c18-primitive-recursive-compiler',9),
 ('p15-goodman-entrenchment','p15/goodman-entrenchment-and-projectibility',3),
 ('p19-self-explanation','p19/self-explanation-and-learning',0),
 ('p19-aging-reasoning','p19/aging-goals-and-reasoning',0),
 ('p15-probability-elimination','p15/probability-quantifier-elimination',7),
 ('p16-cplus-action-language','p16/cplus-action-language',6),
 ('p15-vc-learning','p15/vc-dimension-and-uniform-learning',7),
 ('p09-sos-formats','p09/sos-congruence-and-conservative-extension',8),
 ('p02-free-boolean-completeness','p02/free-boolean-algebra-and-completeness',7),
]
index = sr.ReaderIndex(B)
labels = {k: len(v) for k,v in index.labels.items()}
dynamic = set()
for relative in index.files:
    for m in re.finditer(r'\\showcalculus\s*\{([^}]+)\}', check.strip_comments((B/relative).read_text(encoding='utf-8-sig'))):
        path = B / f'registry/calculi/{m[1]}.tex'
        if path.is_file():
            dynamic.add(path)
for path in dynamic:
    for m in re.finditer(r'\\(?:calculussheet|hbrule)\s*\{([^}]+)\}', check.strip_comments(path.read_text(encoding='utf-8-sig'))):
        labels.setdefault(m[1], 1)
bib = (B/'bib/handbook.bib').read_text(encoding='utf-8-sig')
keys = re.findall(r'@(?!comment\b)[A-Za-z]+\s*\{\s*([^,\s{}]+)', bib, re.I)
errors = list(index.errors)
files = set()
receipts = []
def records(relative):
    files.add(relative)
    if len(index.files.get(relative, [])) != 1:
        errors.append(['route',relative,len(index.files.get(relative,[]))])
    path = B/relative
    text = check.strip_verbatims(check.strip_comments(path.read_text(encoding='utf-8-sig')))
    found = {}
    for m in check.HB_ENV_RE.finditer(text):
        if m[1] in check.HB_STATUS_ENVS or m[1] == 'annexitem':
            fields,_ = check.scan_braced_args(text,m.end(),3)
            if len(fields) != 3:
                errors.append(['arguments',relative,m.start()]); continue
            if fields[0] in found:
                errors.append(['duplicate local result',relative,fields[0]])
            found[fields[0]] = fields
    return text,found
for stem,slug,expected in groups:
    body = f'parts/{slug}.tex'
    bt, br = records(body)
    sources = [{'path': (B/body).relative_to(ROOT).as_posix(), 'sha256': hashlib.sha256((B/body).read_bytes()).hexdigest()}]
    proved = {k:v for k,v in br.items() if v[1].startswith('proved=')}
    annex = f'annex/{slug}.tex'
    if stem == 'p12-equational-basic-completeness':
        annex = 'annex/p12/n-c-035-05-basic-completeness.tex'
    ar = {}
    if expected:
        at,ar = records(annex)
        sources.append({'path':(B/annex).relative_to(ROOT).as_posix(),'sha256':hashlib.sha256((B/annex).read_bytes()).hexdigest()})
    if len(proved) != expected or len(ar) != expected:
        errors.append(['pair count',stem,len(proved),len(ar),expected])
    for key,v in proved.items():
        target = v[1].split('=',1)[1]
        if target not in ar or ar[target][1] != key:
            errors.append(['reciprocal pair',stem,key,target])
    receipts.append({'stem':stem,'source_files':sources,'proved_pairs':len(proved),'body_only':not expected,'standing':'Actual incoming reader integration; no independent source/proof/publication acceptance.'})
files.update(['main.tex','annex/p01-route.tex','parts/p01.tex','parts/p06.tex','annex/p06-route.tex','annex/p07.tex','parts/p09.tex','annex/p09.tex','parts/p15.tex','annex/p15.tex','parts/p16.tex','annex/p16.tex','annex/p12.tex','parts/p07/presentations/coquand-huet-1988.tex','parts/p12/presentations/har2001-c18.tex','parts/p12/presentations/n-c-035-05.tex','parts/p12/presentations/n-c-035-05-narrowing.tex','parts/p06/forcing-variants-supplement.tex','parts/p06/cardinals-choice-supplement.tex','parts/p02/propositional-metatheory-supplement.tex'])
uses=0
for relative in sorted(files):
    text=check.strip_verbatims(check.strip_comments((B/relative).read_text(encoding='utf-8-sig')))
    for m in check.HB_REF_RE.finditer(text):
        uses+=1
        for key in (m[1] or m[2] or '').split(','):
            if key.strip() and labels.get(key.strip(),0)!=1:
                errors.append(['reference',relative,key.strip(),labels.get(key.strip(),0)])
    for m in check.HB_CITE_RE.finditer(text):
        for key in m[1].split(','):
            if key.strip() not in keys:
                errors.append(['citation',relative,key.strip()])
rows,row_errors=sr.read_rows(B/'registry/symbols.csv')
collisions=sr.collision_check(rows)
bodies=[r for r in index.files if r.startswith(('parts/','restoration/'))]
annexes=[r for r in index.files if r.startswith('annex/')]
statuses=collections.Counter()
for relative in bodies:
    text=check.strip_verbatims(check.strip_comments((B/relative).read_text(encoding='utf-8-sig')))
    for m in check.HB_ENV_RE.finditer(text):
        if m[1] in check.HB_STATUS_ENVS:
            fields,_=check.scan_braced_args(text,m.end(),3)
            if len(fields)==3:
                statuses[fields[1].split('=',1)[0]]+=1
summary={'reachable_body_files':len(bodies),'reachable_annex_files':len(annexes),'body_source_lines':sum(len((B/r).read_text(encoding='utf-8-sig').splitlines()) for r in bodies),'editorial_result_statuses':dict(statuses),'editorial_numbered_results':sum(statuses.values()),'route_errors':index.errors}
fulfillment=[]
for p in (ROOT/'spec/coverage/edition-2026/current-fulfillment').glob('*.jsonl'):
    fulfillment.extend(json.loads(line) for line in p.read_text(encoding='utf-8-sig').splitlines())
print(json.dumps({'receipts':receipts,'reader_snapshot':summary,'wire':{'affected_files':len(files),'reference_uses':uses,'dynamic_calculus_files':len(dynamic),'errors':errors,'canonical_row_errors':row_errors,'canonical_collisions':collisions,'canonical_rows':len(rows),'bib_keys':len(keys),'duplicate_bib_keys':sorted(k for k in set(keys) if keys.count(k)>1),'scope':'Incoming route, references, reciprocal declarations and typed notation only; no independent correctness review, build or render.'},'fulfillment_summary':{'sections':len(fulfillment),'unique_sections':len({r['section_id'] for r in fulfillment}),'status_counts':dict(collections.Counter(r['status'] for r in fulfillment))},'coverage_baseline_sha256':hashlib.sha256((ROOT/'spec/edition-2026-coverage-map.json').read_bytes()).hexdigest()},ensure_ascii=False))
