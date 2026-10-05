export const meta = {
  name: 'tmor-acq-r3-download',
  description: 'Download the user-approved acquisition list r3 (14 sources) and verify each file on arrival',
  phases: [{ title: 'Download', detail: 'Opus downloads approved files and verifies identity/version/extent/hash', model: 'opus' }],
}
const S = { type: 'object', properties: {
  entries: { type: 'integer' }, downloaded_verified: { type: 'integer' }, version_differs: { type: 'integer' },
  not_full_body: { type: 'integer' }, failed: { type: 'integer' } },
  required: ['entries', 'downloaded_verified', 'failed'] }
const out = await parallel(args.shards.map(s => () => agent(`Repository C:/Dev/the-methods-of-reason (Windows; Git Bash with curl; Python 3.14 with fitz/pypdf). The user explicitly approved downloading the sources listed in work/waves/w02b/downloads-r3/in-${s}.jsonl (acquisition list r3) in chat on 2026-10-05. Other agents run concurrently: write ONLY under source/references/acq-r3-<ACQ id>/ (one directory per entry) and the result file named below. No git write commands.
Rules: never use shadow libraries (LibGen, Sci-Hub, Anna's Archive, Z-Library or mirrors); never log in, bypass a paywall, CAPTCHA or certificate error; download only from the entry's listed URL/host (following its own link from the landing page to the file is fine; WebFetch may be loaded via ToolSearch "select:WebFetch" to read the landing page). Use \`curl -L --fail --max-time 300 -A "Mozilla/5.0" -o <file> <url>\`.
For each entry:
1. Obtain the full file (PDF preferred; HTML full text saved as .html if that is the only full body). Save as source/references/acq-r3-<ACQ id>/<short-author-year-title>.pdf.
2. Verify with fitz/pypdf: the file opens; page count; title/first pages show the required work (authors, title, container, year; use "identity_corrected" when present); the version matches the required version (or state exactly how it differs: e.g. author preprint vs publisher final; the entry's "version_match" says what the scout and verifier saw); the required extent (pages/sections in the entry) is present with a continuous page sequence (no preview/truncation).
3. sha256 and bytes.
4. Write source/references/acq-r3-<ACQ id>/manifest.json: {"acq_id","source_key":<entry key>,"units":[...],"work":<required work, corrected citation if given>,"required_version":...,"files":[{"path":"source/references/acq-r3-.../file","sha256","bytes","pdf_pages","version":"<as seen on the document>","extent_verified":true|false,"extent_note":"..."}],"identity_seen":"...","access_basis":"<host_kind and url>","downloaded_utc":"<now>","approval":"user chat approval 2026-10-05 (acquisition list r3)"}.
5. If the download fails, or the file is a different work, a preview or truncated, delete the file, keep the manifest with "files":[] and a precise "failure" field.
Write work/waves/w02b/downloads-r3/out-${s}.jsonl, one line per entry: {"acq_id","key","result":"downloaded_verified|version_differs|not_full_body|failed","detail","path","sha256"}. Return counts.`,
  { model: 'opus', effort: 'high', schema: S, label: `dl3:${s}`, phase: 'Download' })))
const ok = out.filter(Boolean)
const sum = k => ok.reduce((n, r) => n + (r[k] || 0), 0)
return { shards: ok.length, entries: sum('entries'), downloaded_verified: sum('downloaded_verified'), version_differs: sum('version_differs'), not_full_body: sum('not_full_body'), failed: sum('failed') }