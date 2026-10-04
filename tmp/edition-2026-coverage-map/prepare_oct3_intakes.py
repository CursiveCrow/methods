"""Prepare Oct3 append-only intake proposals; NEVER write canonical files.

Reads only batch3 and its two named followons, not old merged intake batches.
All output is adjacent oct3-intake-proposal JSON/patch data. Root owns decisions.
"""
from __future__ import annotations
import argparse, copy, csv, hashlib, io, json, re, sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
BASE = ROOT / "handbook"
sys.path.insert(0, str(ROOT / "tools"))
import check as grammar
import symbol_registry as registry

FIELDS = registry.HEADER
def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()
def read(path): return path.read_text(encoding="utf-8-sig")
def write_json(name, data):
    path = OUT / ("oct3-intake-proposal-" + name + ".json")
    assert path.parent == OUT and path.name.startswith("oct3-intake-proposal-")
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return path.name
def write_patch(name, target, old, new):
    if not new: return None
    path = OUT / ("oct3-intake-proposal-" + name + ".patch")
    assert path.parent == OUT
    text = "*** Begin Patch\n*** Update File: " + target.as_posix() + "\n@@\n"
    text += "\n".join(" " + line for line in old.splitlines()) + "\n"
    text += "\n".join("+" + line for line in new.splitlines()) + "\n*** End Patch\n"
    path.write_text(text, encoding="utf-8")
    return path.name
def csv_lines(rows, header=False):
    s = io.StringIO(newline="")
    w = csv.DictWriter(s, fieldnames=FIELDS, lineterminator="\n")
    if header: w.writeheader()
    w.writerows({k: r[k] for k in FIELDS} for r in rows)
    return s.getvalue().rstrip("\n")
def tuple_row(r): return tuple(r.get(k, "") for k in FIELDS)
def public(r): return {k: v for k, v in r.items() if not k.startswith("_")}
def excluded(r): return r.get("_already_merged",False) or r.get("_root_reuse",False)
def rid(r): return r.get("_uid",str(r["_line"]))

def cumulative_chunks(kind, target, anchor, units, *, json_members=False):
    """Ordered append chunks with actual/virtual tail anchors, under8000 chars."""
    names=[]; number=0; current=anchor; batch=[]
    def render(old, chosen):
        if json_members:
            addition=",\n"+",\n".join(chosen)
            replacement=old+addition
            return "*** Begin Patch\n*** Update File: "+target.as_posix()+"\n@@\n"+"\n".join("-"+x for x in old.splitlines())+"\n"+"\n".join("+"+x for x in replacement.splitlines())+"\n*** End Patch\n"
        return "*** Begin Patch\n*** Update File: "+target.as_posix()+"\n@@\n"+"\n".join(" "+x for x in old.splitlines())+"\n"+"\n".join("+"+x for x in "\n".join(chosen).splitlines())+"\n*** End Patch\n"
    def flush():
        nonlocal number,current,batch
        if not batch:return
        number+=1; text=render(current,batch)
        if len(text)>=8000:raise ValueError((kind,"single unit exceeds chunk limit",len(text)))
        path=OUT/("oct3-intake-proposal-cumulative-"+kind+"-%02d.patch"%number)
        path.write_text(text,encoding="utf-8");names.append(path.name)
        current=batch[-1] if kind in {"bib","scopes"} else batch[-1].splitlines()[-1]
        batch=[]
    for unit in units:
        if batch and len(render(current,batch+[unit]))>=7800:flush()
        batch.append(unit)
    flush();return names

def bib_records(text):
    records = []
    for m in re.finditer(r"@([A-Za-z]+)\s*\{\s*([^,\s{}]+)\s*,", text):
        if m[1].lower() in {"comment", "string", "preamble"}: continue
        brace = text.find("{", m.start())
        args, end = grammar.scan_braced_args(text, brace, 1)
        if not args: raise ValueError("Unbalanced bibliography record " + m[2])
        raw = text[m.start():end]
        # Exact records are compared without external source equivalence.
        records.append({"key": m[2], "type": m[1].lower(), "raw": raw,
                        "sha256": hashlib.sha256(raw.encode()).hexdigest(),
                        "comparison": re.sub(r"\s+", " ", grammar.strip_comments(raw)).strip()})
    return records

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--stem", action="append", help="Optional current group selection")
    args = ap.parse_args()
    manifest = ROOT / "spec/research/edition-2026-authoring-batch-intake-3.json"
    groups = json.loads(read(manifest))["groups"]
    groups += [
        {"stem":"p07-girard-empires","part":"P7",
         "bodies":["parts/p07/girard-trips-and-empires.tex"],
         "annex":"annex/p07/girard-trips-and-empires.tex"},
        {"stem":"p10-domain-invariance","part":"P10",
         "bodies":["parts/p10/domain-recursion-and-invariance.tex"],
         "annex":"annex/p10/domain-recursion-and-invariance.tex"},
        {"stem":"p14-reference-repairs","part":"P14","bodies":[],"annex":None,"symbols":False},
    ]
    # Followon filename is discovered from the exact first-use declarations,
    # not guessed from the display title.
    for g in groups:
        if g["stem"] == "p07-girard-empires":
            for zone in ("parts", "annex"):
                hits = [p for p in (BASE/zone/"p07").glob("*.tex")
                        if "p07-girard-empire-interval" in read(p) or
                        (zone == "annex" and "annex:p07.girard-empire" in read(p))]
                if len(hits) == 1:
                    rel = hits[0].relative_to(BASE).as_posix()
                    if zone == "parts": g["bodies"] = [rel]
                    else: g["annex"] = rel
    if args.stem:
        groups = [g for g in groups if g["stem"] in args.stem]
        unknown = set(args.stem) - {g["stem"] for g in groups}
        if unknown: raise ValueError("Unknown current group(s): " + repr(unknown))

    canonical = [BASE/"registry/symbols.csv", BASE/"registry/symbol-scopes.json", BASE/"bib/handbook.bib"]
    snapshots = {p.relative_to(ROOT).as_posix(): {"sha256":sha(p), "text":read(p)} for p in canonical}
    old_rows = list(csv.DictReader(io.StringIO(snapshots["handbook/registry/symbols.csv"]["text"])))
    old_keys = {tuple_row(r) for r in old_rows}
    bindings = json.loads(snapshots["handbook/registry/symbol-scopes.json"]["text"])
    index = registry.ReaderIndex(BASE)
    pending_routes = []
    # Prospective preparation is explicitly separate from current routing.
    # Read actual frozen source files into an in-memory declaration index only;
    # leave their chapter ordinals unbound rather than invent a placement rank.
    for g in groups:
        paths = list(g.get("bodies", [])) + ([g["annex"]] if g.get("annex") else [])
        if g["stem"] == "p07-girard-empires":
            paths = ["parts/p07/girard-1987-trips-and-empires.tex",
                     "annex/p07/girard-1987-trips-and-empires.tex"]
            g["bodies"], g["annex"] = paths[:1], paths[1]
        for rel in paths:
            if not (BASE/rel).is_file(): continue
            if len(index.files.get(rel, [])) == 0:
                index._close_headings(0)
                index._visit(rel, int(g["part"][1:]))
                index._close_headings(0)
                pending_routes.append(rel)
                for ds in index.labels.values():
                    for d in ds:
                        if d.path == rel: d.chapter = None
                for h in index.heading_records:
                    if h.path == rel: h.chapter = None
                for region in index.files.get(rel, []): region.chapter = None
    new_bindings, datasets, issues = {}, {}, []
    for g in groups:
        stem = g["stem"]
        path = BASE / ("registry/symbols-intake-" + stem + ".csv")
        rows = []
        if g.get("symbols") is not False:
            if not path.exists(): issues.append({"group":stem,"kind":"missing-symbol-intake","path":str(path)})
            else:
                with path.open(encoding="utf-8-sig", newline="") as f:
                    reader = csv.DictReader(f)
                    if reader.fieldnames != FIELDS: raise ValueError((path, reader.fieldnames))
                    for line, raw in enumerate(reader, 2):
                        if None in raw: raise ValueError((path,line,"malformed CSV field count"))
                        row = {k:(raw[k] or "").strip() for k in FIELDS}
                        row.update(_group=stem, _line=line, _original=copy.deepcopy(row))
                        changes = []
                        if not row["macro"]:
                            glyph = row["glyph"]
                            row["macro"] = glyph[2:-2] if glyph.startswith(r"\(") and glyph.endswith(r"\)") else glyph
                            changes.append("Blank macro filled with exact unchanged glyph spelling; this is data, not a newly defined TeX macro.")
                        if not registry.PREC_RE.fullmatch(row["precedence"]):
                            original = row["precedence"]
                            row["precedence"] = "n/a"
                            changes.append("Original precedence descriptor " + repr(original) + " preserved as semantic metadata; n/a is not an invented binding rank.")
                        if changes: row["notes"] += (" " if row["notes"] else "") + " ".join(changes)
                        row["_changes"] = changes
                        row["_already_merged"] = tuple_row(raw) in old_keys or tuple_row(row) in old_keys
                        rows.append(row)
        datasets[stem] = {"group":g,"symbol_path":path,"rows":rows}

    root_decisions=[]
    def child(row,glyph,role,scope,first=None):
        r=copy.deepcopy(row);r["glyph"]=glyph;r["macro"]=glyph[2:-2]
        r["role"]=role;r["scope"]=scope;r["first_use"]=first or row["first_use"]
        r["_uid"]=str(row["_line"])+":"+glyph+":"+role
        r["notes"] += " Root-authorized typed split; original grouped intake row remains unchanged as evidence."
        r["_already_merged"]=tuple_row(r) in old_keys
        return r
    for stem,data in datasets.items():
        transformed=[]
        for row in data["rows"]:
            if stem=="p12-drat-checking" and row["glyph"]==r"\(v\)" and row["role"]=="total Boolean valuation":
                matches=[r for r in old_rows if r["glyph"]==r"\(v\)" and r["scope"]=="global" and r["role"]=="valuation"]
                if len(matches)!=1:raise ValueError("Root v reuse selector is not unique")
                row["_root_reuse"]=True
                root_decisions.append({"decision":"reuse-canonical-v","incoming":public(row),"canonical":matches[0],"reason":"Root identifies the total Boolean case as specialization of the existing global valuation role, not a new row."})
            if stem=="p19-motivated-reasoning" and row["glyph"]==r"\(p,q\)":
                children=[child(row,r"\(p\)","antecedent category property in the selection example",row["scope"]),child(row,r"\(q\)","consequent category property in the selection example",row["scope"])]
                root_decisions.append({"decision":"split-selection-properties","original":row["_original"],"children":[public(r) for r in children]})
                transformed.extend(children);continue
            if stem=="p16-best-explanation" and row["glyph"]==r"\(R,B,H_0,H_1\)":
                children=[child(row,r"\(R\)","unary raven predicate in the logical comparison","P16 IBE raven logical predicates"),child(row,r"\(B\)","unary black predicate in the logical comparison","P16 IBE raven logical predicates"),child(row,r"\(B\)","selected-object blackness event in the sampling calculation","P16 IBE raven sampling events","def:p16-ibe-raven-sampling"),child(row,r"\(H_0\)","population alternative with both ravens black","P16 IBE raven sampling events","def:p16-ibe-raven-sampling"),child(row,r"\(H_1\)","population alternative with one black and one nonblack raven","P16 IBE raven sampling events","def:p16-ibe-raven-sampling")]
                root_decisions.append({"decision":"split-raven-logical-and-sampling-types","original":row["_original"],"children":[public(r) for r in children]})
                transformed.extend(children);continue
            transformed.append(row)
        data["rows"]=transformed

    def local_regions(first, group):
        d = index.unique(first)
        if d.path.startswith("annex/"):
            specs = [{"anchor":d.label}]
            if d.owner:
                owner = index.unique(d.owner)
                specs.append({"anchor":owner.label})
            return specs
        # Bind to real containing headings, never to a fabricated filename namespace.
        headings = [h for h in index.heading_records if h.path == d.path and h.start <= d.start < h.end]
        h = max(headings, key=lambda x:x.start) if headings else None
        specs = [{"heading_of":first,"level":h.kind}] if h else [{"anchor":first}]
        region = index.region(specs[0])
        for ds in index.labels.values():
            for a in ds:
                if a.kind == "annexitem" and a.owner and a.path == group.get("annex"):
                    owner = index.unique(a.owner)
                    if region.start <= owner.start < region.end: specs.append({"anchor":a.label})
        return specs

    for stem, data in datasets.items():
        by_scope = {}
        for row in data["rows"]:
            if excluded(row): continue
            by_scope.setdefault(row["scope"], []).append(row)
        for name, rs in by_scope.items():
            if registry.parse_scope(name) or registry.LABEL_RE.fullmatch(name) or " through " in name: continue
            if name in bindings["scopes"]: continue
            specs = []
            for r in rs:
                try: specs.extend(local_regions(r["first_use"],data["group"]))
                except registry.RegistryError as e:
                    issues.append({"group":stem,"kind":"binding-unresolved","scope":name,"first_use":r["first_use"],"error":str(e)})
            unique = list({json.dumps(s,sort_keys=True):s for s in specs}.values())
            if unique:
                new_bindings[name] = {"presentation":"Actual frozen author-return group " + stem + "; current local types only, no source/version admission",
                                      "regions":unique}
    # An explicitly composed alias is the union of its existing real aliases,
    # not a disjoint namespace invented for a conflicting role.
    for name, binding in list(new_bindings.items()):
        parts = name.split(" and ")
        pool = {**bindings["scopes"],**new_bindings}
        if len(parts) == 2 and all(p in pool for p in parts):
            binding["regions"] = list({json.dumps(r,sort_keys=True):r for p in parts for r in pool[p]["regions"]}.values())
    def bind(name,regions,presentation):
        if name not in new_bindings:
            new_bindings[name]=copy.deepcopy(bindings["scopes"].get(name,{"presentation":presentation,"regions":regions}))
        new_bindings[name]["regions"]=regions
        new_bindings[name]["presentation"]=presentation
        return new_bindings[name]
    def override(name,row,broader_scope,broader_role,source,reason):
        if name not in new_bindings:
            bind(name,[{"anchor":name}],source+"; explicit root-authorized typed role")
        rule={"glyph":row["glyph"],"local_role":row["role"],"first_use":row["first_use"],"broader_scope":broader_scope,"broader_role":broader_role,"source":source,"reason":reason}
        existing_rules=new_bindings[name].setdefault("overrides",[])
        if rule not in existing_rules:existing_rules.append(rule)
        root_decisions.append({"decision":"exact-typed-override","scope":name,"override":rule})
    for row in datasets.get("p03-imaginaries",{}).get("rows",[]):
        if row["glyph"]==r"\(s\)":override(row["scope"],row,"global","variable assignment","Speirs2013Imaginaries","The current uniform-code theorem explicitly declares s:D->D a definable E-class-invariant selector. It is not a first-order variable assignment; root directs retention of this exact local function role.")
    for row in datasets.get("p12-drat-checking",{}).get("rows",[]):
        scope=row["scope"]
        if row["glyph"]==r"\(s\)":override(scope,row,"global","variable assignment","WetzlerHeuleHunt2014AuthorDRAT","The truth-tree declaration types s as a finite variable-prefix assignment including empty/full prefixes. Root preserves this partial propositional construction role against the global first-order assignment role.")
        if row["role"]=="CNF multiset in the separately dated 2016 interpretation":override(scope,row,"sec:p12-drat-certificates-and-checking","finite CNF clause-set database","Heule2016DRATFormatV1","The current2016 definition expressly retypes F as a multiset with single-copy deletion, distinct from the2014 set database. Root retains both versions without equating their update policies.")
        if row["role"]=="nonzero signed integer literal code in 2016 serialization":override(scope,row,"sec:p12-drat-certificates-and-checking","abstract signed propositional literal","Heule2016DRATFormatV1","The binary serialization paragraph expressly types l as a nonzero signed integer code and gives2l/-2l+1 encoding. This locally declared representation is distinct from an abstract signed literal.")
        if row["role"]=="empty clause-set database":override(scope,row,scope,"empty literal-set clause","WetzlerHeuleHunt2014AuthorDRAT","The SAME finite-CNF definition explicitly declares an empty literal-set clause false and an empty clause-set database true. Root directs retention of both typed readings in this same declaration region; argument type, not a fabricated disjoint scope, distinguishes them.")
    if "p19-motivated-reasoning" in datasets:
        bind("P19 motivated reasoning selection example",[{"anchor":"def:p19-mrg-selection-case"}],"DawsonGilovichRegan2002WasonMRG context with explicitly stipulated local selection schema")
        bind("P19 motivated reasoning empirical records",[{"file":"parts/p19/motivated-reasoning-and-goals.tex"}],"Separately attributed current empirical report regions; significance notation is not the local selection property")
        for row in datasets["p19-motivated-reasoning"]["rows"]:
            if row["role"]=="antecedent category property in the selection example":override(row["scope"],row,"P19 motivated reasoning empirical records","reported significance probability","DawsonGilovichRegan2002WasonMRG","The selection-case declaration types p as a category property. The empirical reports use p for significance probabilities. Root permits a whole-file empirical scope with this exact declaration-local property exception and will add pre-study notation prose.")
    if "p16-best-explanation" in datasets:
        bind("P16 IBE raven logical predicates",[{"anchor":"thm:p16-ibe-raven-logic"},{"anchor":"annex:p16.ibe-raven-logic"}],"Lipton2004BestExplanation context; explicitly declared R/B logical predicates")
        bind("P16 IBE raven sampling events",[{"anchor":"def:p16-ibe-raven-sampling"},{"anchor":"thm:p16-ibe-raven-sampling"},{"anchor":"annex:p16.ibe-raven-sampling"}],"Lipton2004BestExplanation context; separately stipulated finite sampling model and explicit B event retyping")
    combined = copy.deepcopy(bindings)
    combined["scopes"].update(new_bindings)
    resolver = registry.Resolver(BASE, bindings=combined, index=index)
    # Proposed bibliography records are identified separately; root applies
    # their append chunks BEFORE scopes whose override schema cites these keys.
    for g in groups:
        path=BASE/("bib/intake-"+g["stem"]+".bib")
        if path.exists():resolver.source_keys.update(r["key"] for r in bib_records(read(path)))
    parsed_old, canonical_errors = registry.read_rows(BASE/"registry/symbols.csv", resolver=resolver)
    all_new = []
    for stem,data in datasets.items():
        for row in data["rows"]:
            if excluded(row): continue
            row["_resolver"] = resolver
            try:
                row["_scope"] = resolver.resolve(row["scope"])
                if not resolver.contains(row["_scope"],row["first_use"]): raise registry.RegistryError("first_use outside resolved scope")
                all_new.append(row)
            except registry.RegistryError as e: issues.append({"group":stem,"kind":"row-unresolved","line":row["_line"],"row":public(row),"error":str(e)})
    # Pair checks retain exact actual overlapping regions; no automatic overrides.
    collisions, held = [], set()
    glyphs = {}
    for r in parsed_old + all_new: glyphs.setdefault(re.sub(r"\s+","",r["glyph"]),[]).append(r)
    for entries in glyphs.values():
        for i,a in enumerate(entries):
            for b in entries[i+1:]:
                if not (a.get("_group") or b.get("_group")): continue
                if not resolver.overlaps(a["_scope"],b["_scope"]): continue
                if a["role"] != b["role"] and (resolver.authorized_override(a,b) or resolver.authorized_override(b,a)): continue
                for r in (a,b):
                    if r.get("_group"): held.add((r["_group"],rid(r)))
                collisions.append({"kind":"duplicate-glyph-role" if a["role"] == b["role"] else "typed-role-overlap",
                    "glyph":a["glyph"],"a":{**public(a),"group":a.get("_group","canonical"),"line":a["_line"]},
                    "b":{**public(b),"group":b.get("_group","canonical"),"line":b["_line"]},
                    "decision":"HELD for root: same actual reader regions overlap; no glyph rename, fake disjoint scope, invented rank or automatic semantic alias."})

    old_bib = bib_records(snapshots["handbook/bib/handbook.bib"]["text"])
    by_key = {}
    for b in old_bib: by_key.setdefault(b["key"], []).append(b)
    bib_decisions = []
    files = []; cumulative_rows=[]; cumulative_bib=[]
    for stem,data in datasets.items():
        new_bib, decisions = [], []
        bp = BASE / ("bib/intake-"+stem+".bib")
        if bp.exists():
            for rec in bib_records(read(bp)):
                previous = by_key.get(rec["key"],[])
                if previous:
                    identical = any(rec["comparison"] == p["comparison"] for p in previous)
                    decision = "skip-identical-record" if identical else "hold-conflicting-key"
                    d = {"group":stem,"key":rec["key"],"decision":decision,"incoming":rec,
                         "existing":previous,"standing":"Exact full record comparison, not title-based source equivalence. Differing notes/versions/manifestations require root decision."}
                    decisions.append(d);bib_decisions.append(d)
                else:
                    new_bib.append(rec);by_key.setdefault(rec["key"],[]).append(rec)
        safe = [r for r in data["rows"] if not excluded(r) and "_scope" in r and (stem,rid(r)) not in held]
        cumulative_rows.extend(safe);cumulative_bib.extend(new_bib)
        own_bindings = {r["scope"]:new_bindings[r["scope"]] for r in data["rows"] if r["scope"] in new_bindings}
        candidate = {"stem":stem,"route_pending_files":[p for p in pending_routes if p in data["group"].get("bodies",[]) or p == data["group"].get("annex")],
          "inputs":[{"path":p.relative_to(ROOT).as_posix(),"sha256":sha(p)} for p in (data["symbol_path"],bp) if p.exists()],
          "source_region_files":[{"path":"handbook/"+rel,"sha256":sha(BASE/rel),"route_pending":rel in pending_routes}
            for rel in data["group"].get("bodies",[])+([data["group"]["annex"]] if data["group"].get("annex") else []) if (BASE/rel).exists()],
          "proposed_rows":[public(r) for r in safe],"held_rows":[public(r) for r in data["rows"] if (stem,rid(r)) in held],
          "reused_canonical_rows":[public(r) for r in data["rows"] if r.get("_root_reuse")],
          "already_merged_lines":[r["_line"] for r in data["rows"] if r["_already_merged"]],
          "normalizations":[{"line":r["_line"],"original":r["_original"],"normalized":public(r),"changes":r["_changes"]} for r in data["rows"] if r["_changes"]],
          "new_scope_bindings":own_bindings,"new_bib_records":new_bib,"bib_duplicate_decisions":decisions}
        files.append(write_json(stem,candidate))
        if own_bindings:
            files.append(write_json(stem+"-scopes",{"append_only_scopes":own_bindings,
              "route_pending_files":candidate["route_pending_files"],
              "standing":"Exact prospective/current declaration selectors, not assigned chapter ordinals; root applies to latest canonical scopes."}))
        # Per-group JSON remains evidence, but only the ordered cumulative
        # chunks below are applicable in this root-decision update.
    # Scope fragments are intentionally JSON: root applies exact member additions
    # against its latest canonical file, without a giant replace-file patch.
    files.append(write_json("scopes",{"schema_version":1,"append_only_scopes":new_bindings,
        "standing":"Selectors are actual labelled headings/declaration regions, with exact associated annex items. No scope splits suppress typed overlaps."}))
    application_order={}
    application_order["bib"]=cumulative_chunks("bib",BASE/"bib/handbook.bib",old_bib[-1]["raw"],[b["raw"] for b in cumulative_bib])
    scope_text=snapshots["handbook/registry/symbol-scopes.json"]["text"]
    old_last=next(reversed(bindings["scopes"]))
    literal_key=json.dumps(old_last,ensure_ascii=False)
    tokenpos=scope_text.rfind(literal_key)
    if tokenpos<0:raise ValueError("Cannot locate exact canonical last scope")
    keypos=scope_text.rfind('\n',0,tokenpos)+1
    valuepos=scope_text.index(':',tokenpos+len(literal_key))+1
    while scope_text[valuepos].isspace():valuepos+=1
    _,extent=json.JSONDecoder().raw_decode(scope_text[valuepos:])
    anchor=scope_text[keypos:valuepos+extent]
    prefix=scope_text[keypos:tokenpos]
    def member(k,v):return '\n'.join(prefix+line[2:] for line in json.dumps({k:v},ensure_ascii=False,indent=2).splitlines()[1:-1])
    existing_updates={k:v for k,v in new_bindings.items() if k in bindings["scopes"] and v!=bindings["scopes"][k]}
    if existing_updates:issues.append({"kind":"existing-scope-update-held","names":list(existing_updates),"reason":"Root must append exact overrides to existing objects; cumulative scope append excludes replacements."})
    application_order["scopes"]=cumulative_chunks("scopes",BASE/"registry/symbol-scopes.json",anchor,[member(k,v) for k,v in new_bindings.items() if k not in bindings["scopes"]],json_members=True)
    application_order["rows"]=cumulative_chunks("rows",BASE/"registry/symbols.csv",snapshots["handbook/registry/symbols.csv"]["text"].rstrip().splitlines()[-1],[csv_lines([r]) for r in cumulative_rows])
    files.extend(p for ps in application_order.values() for p in ps)
    virtual={"bib":snapshots["handbook/bib/handbook.bib"]["text"],"scopes":scope_text,"rows":snapshots["handbook/registry/symbols.csv"]["text"]}
    replay_errors=[];chunk_sizes={}
    for kind in ("bib","scopes","rows"):
        for name in application_order[kind]:
            patch=read(OUT/name);chunk_sizes[name]=len(patch)
            if len(patch)>=8000:replay_errors.append(name+": chunk limit")
            hunk=patch.split('@@\n',1)[1].rsplit('*** End Patch',1)[0].rstrip('\n').splitlines()
            old='\n'.join(line[1:] for line in hunk if line[:1] in {' ','-'})
            new='\n'.join(line[1:] for line in hunk if line[:1] in {' ','+'})
            if virtual[kind].count(old)!=1:replay_errors.append(name+": nonunique/missing cumulative anchor")
            else:virtual[kind]=virtual[kind].replace(old,new,1)
    try:
        virtual_scopes=json.loads(virtual["scopes"])
        virtual_rows=list(csv.DictReader(io.StringIO(virtual["rows"])))
        virtual_bib=bib_records(virtual["bib"])
        if len(virtual_rows)!=len(old_rows)+len(cumulative_rows):replay_errors.append("Cumulative CSV count mismatch")
        if set(new_bindings)-set(virtual_scopes["scopes"]):replay_errors.append("Cumulative scopes omitted a binding")
        if len(virtual_bib)!=len(old_bib)+len(cumulative_bib):replay_errors.append("Cumulative bibliography count mismatch")
    except (ValueError,csv.Error) as e:replay_errors.append(str(e))
    files.append(write_json("root-decisions",{"root_authorization":"Explicit root decisions in this update task; original intakes preserved","decisions":root_decisions,"application_order":application_order,"chunk_characters":chunk_sizes,"in_memory_cumulative_parsing_errors":replay_errors,"supersedes":"Earlier non-cumulative per-group PATCH files are historical and must not be applied; use only this ordered cumulative list.","pending_root_manuscript_action":"Add the pre-study P19 significance/property notation declaration; proposal preparation does not claim it already exists.","existing_scope_updates_held":existing_updates,"standing":"No canonical writes, source equivalence or admission certification."}))
    after = {p.relative_to(ROOT).as_posix():sha(p) for p in canonical}
    summary = {"utc":datetime.now(timezone.utc).isoformat(),"manifest_sha256":sha(manifest),
      "canonical_before":{k:v["sha256"] for k,v in snapshots.items()},"canonical_after":after,
      "canonical_changed_during_read":[k for k,v in snapshots.items() if v["sha256"] != after[k]],
      "groups":[g["stem"] for g in groups],"route_pending_files":pending_routes,"new_scope_count":len(new_bindings),
      "proposed_row_count":sum(1 for r in all_new if (r["_group"],rid(r)) not in held),
      "root_decisions":root_decisions,"application_order":application_order,"chunk_characters":chunk_sizes,"in_memory_cumulative_parsing_errors":replay_errors,
      "held_row_count":len(held),"normalization_count":sum(bool(r["_changes"]) for d in datasets.values() for r in d["rows"]),
      "canonical_read_errors":canonical_errors,"reader_index_errors":index.errors,
      "issues":issues,"collisions":collisions,"bib_duplicate_decisions":bib_decisions,"files":files,
      "standing":"Intake preparation only. Script writes adjacent proposal files, never canonical files or manuscript. Root owns all merge/override/version decisions. Patch tail anchors and hashes are snapshot-specific; rerun selected groups after a root merge. No implementation tests, proof review, build, render or source acquisition."}
    write_json("summary",summary)
    print(json.dumps({k:summary[k] for k in ("utc","groups","new_scope_count","proposed_row_count","held_row_count","normalization_count","canonical_changed_during_read")},ensure_ascii=False))
    print("OUTPUT oct3-intake-proposal-summary.json")

if __name__ == "__main__": main()
