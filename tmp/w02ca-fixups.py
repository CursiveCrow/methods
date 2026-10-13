"""w02ca return fixups after normalize_returns: returns with no new routed file get placement null;
p15-010's comment-only files get their input."""
import json, glob
N = 'work/waves/w02ca/returns-normalized'
def ld(s):
    p = glob.glob(f'{N}/*w02c-{s}-return.json')[0]
    return p, json.load(open(p, encoding='utf-8'))
for s in ('p02-008', 'p02-030', 'p02-031', 'p15-018', 'p02-002', 'p15-006'):
    p, d = ld(s); d['placement_note'] = d.get('placement'); d['placement'] = None
    json.dump(d, open(p, 'w', encoding='utf-8', newline='\n'), ensure_ascii=False, indent=1)
p, d = ld('p15-010')
d['placement']['body']['input'] = 'parts/p15/conditioning-independence-and-information-w02c-p15-010'
d['placement']['annex']['input'] = 'annex/p15/conditioning-independence-and-information-w02c-p15-010'
json.dump(d, open(p, 'w', encoding='utf-8', newline='\n'), ensure_ascii=False, indent=1)
