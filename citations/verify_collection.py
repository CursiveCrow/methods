"""Verify retained files, catalogue consistency, and optional original sources."""
import argparse,csv,hashlib,json,pathlib,re,unicodedata
from urllib.parse import unquote
def digest(path):
 h=hashlib.sha256()
 with path.open('rb') as f:
  for b in iter(lambda:f.read(1024*1024),b''):h.update(b)
 return h.hexdigest()
def main():
 parser=argparse.ArgumentParser();parser.add_argument('directory',nargs='?',default=str(pathlib.Path(__file__).parent));parser.add_argument('--sources',action='store_true');a=parser.parse_args()
 root=pathlib.Path(a.directory).resolve();manifest=json.loads((root/'manifest.json').read_text(encoding='utf-8'));original_root=pathlib.Path(manifest['source_root']);entries=manifest['entries'];names={e['filename'] for e in entries}
 assert len(entries)==len(names)==manifest['summary']['resource_files'];source_hashes={};extracted_pages=0
 for e in entries:
  p=root/e['filename'];assert p.resolve().parent==root and p.is_file();assert p.stat().st_size==e['bytes'] and digest(p)==e['sha256'],p
  if e['format']=='PDF' and e['verification'].get('original_bytes_preserved_as_prefix'):
   with p.open('rb') as f:assert hashlib.sha256(f.read(e['source_bytes'])).hexdigest()==e['source_sha256'],p
  if a.sources:
   for relative in e['original_paths']:
    original=original_root/relative
    if str(original) not in source_hashes:source_hashes[str(original)]=digest(original)
    assert source_hashes[str(original)]==e['source_sha256'],original
  if 'source_page_range_zero_based' in e:
   start,end=e['source_page_range_zero_based'];assert e['pages']==end-start+1
   assert e['verification']['all_extracted_page_rasters_identical']==end-start+1
   if a.sources:
    import pymupdf as fitz
    with fitz.open(original_root/e['original_paths'][0]) as src,fitz.open(p) as dst:
     assert len(dst)==end-start+1
     assert dst.metadata['title']==e['bibliographic_metadata']['title'] and dst.metadata['author']==e['bibliographic_metadata']['author']
     for i in range(len(dst)):
      assert src[start+i].get_text()==dst[i].get_text()
      assert src[start+i].get_pixmap(alpha=False).samples==dst[i].get_pixmap(alpha=False).samples
      extracted_pages+=1
 with (root/'metadata.csv').open(encoding='utf-8-sig',newline='') as f:rows=list(csv.DictReader(f))
 assert len(rows)==len(entries) and {r['filename'] for r in rows}==names
 byname={e['filename']:e for e in entries}
 for row in rows:
  e=byname[row['filename']];assert row['sha256']==e['sha256'] and row['title']==e['bibliographic_metadata']['title'] and row['author']==e['bibliographic_metadata']['author']
 keys=[''.join(c for c in unicodedata.normalize('NFKC',e['bibliographic_metadata']['title']).casefold() if c.isalnum()) for e in entries]
 assert len(keys)==len(set(keys))
 links=re.findall(r'\]\(([^\n]+?)\)',(root/'README.md').read_text(encoding='utf-8'))
 for link in links:assert (root/unquote(link)).exists(),link
 with (root/'FILENAME-MAP.csv').open(encoding='utf-8-sig',newline='') as f:aliases=list(csv.DictReader(f))
 assert all(r['copied_filename'] in names for r in aliases)
 with (root/'REMOVALS.csv').open(encoding='utf-8-sig',newline='') as f:removed=list(csv.DictReader(f))
 assert len(removed)==manifest['cleanup']['old_resource_files_removed']
 for r in removed:assert not (root/r['removed_filename']).exists(),r['removed_filename']
 allowed={'README.md','manifest.json','metadata.csv','FILENAME-MAP.csv','REMOVALS.csv','VERIFICATION.json','verify_collection.py'}
 assert {p.name for p in root.iterdir()}==names|allowed
 print(json.dumps({'resource_files_verified':len(entries),'metadata_rows_verified':len(rows),'local_links_verified':len(links),'removed_files_confirmed_absent':len(removed),'original_source_files_verified':len(source_hashes),'extracted_pages_reverified':extracted_pages,'filename_map_rows':len(aliases),'duplicate_normalized_titles':0}))
if __name__=='__main__':main()
