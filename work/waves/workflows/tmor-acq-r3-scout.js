export const meta = {
  name: 'tmor-acq-r3-scout',
  description: 'Acquisition list r3: free-copy search for 42 unresolved sources, then independent identity verification (no downloads)',
  phases: [
    { title: 'Scout', detail: 'Opus search for lawful freely reachable full copies; no downloads', model: 'opus' },
    { title: 'Verify', detail: 'fresh Opus verifies each candidate', model: 'opus' },
  ],
}
const LIMIT = 7
let active = 0; const waiters = []
const acquire = () => active < LIMIT ? (active++, Promise.resolve()) : new Promise(r => waiters.push(r))
const release = () => { const n = waiters.shift(); if (n) n(); else active-- }
const run = async (p, o) => { await acquire(); try { return await agent(p, o) } finally { release() } }
const D = 'work/waves/w02b/scout3'
const COMMON = `Repository C:/Dev/the-methods-of-reason. Other agents run concurrently: write ONLY the output file named below. No git write commands. Never download any file (landing pages and catalogue records only, via WebSearch/WebFetch loaded with ToolSearch "select:WebSearch,WebFetch"). Never shadow libraries (LibGen, Sci-Hub, Anna's Archive, Z-Library, mirrors) and never borrow-only/controlled-digital-lending items that require login.`
const SC = { type: 'object', properties: { searched: { type: 'integer' }, candidates: { type: 'integer' }, still_none: { type: 'integer' } }, required: ['searched', 'candidates', 'still_none'] }
const VE = { type: 'object', properties: { checked: { type: 'integer' }, confirmed: { type: 'integer' }, rejected: { type: 'integer' } }, required: ['checked', 'confirmed', 'rejected'] }
const out = await pipeline(args.shards,
  s => run(`${COMMON}
TASK: the sources in ${D}/in-${s}.jsonl (each line: acq_id, key, work, required version, extent, units, sections) were raised by assessors as needed and not held; they have not been searched yet. Their bibliographic details come from assessors and may be imprecise: first establish the exact work (authors, title, container, year, pages, DOI) from catalogue records (publisher page, DOI resolver, DBLP, zbMATH, MathSciNet-free listings, library catalogues), and record any correction. Then search for a lawful freely reachable full copy of EXACTLY the required work and version: publisher open archives, the author's homepage or institutional page (including archived copies on web.archive.org), institutional/university repositories (eprints, DSpace, HAL, PhilArchive, CiteSeerX, Semantic Scholar/Unpaywall OA links, arXiv/SSRN/RePEc), conference/proceedings open archives, digitized public-domain or full-view books (HathiTrust full view, Internet Archive public-domain/full-view items only, Gallica, EuDML, Numdam, GDZ, Google Books full view), course pages and university sites hosting the paper (acceptable per the user). Identify a different edition/printing only when the record shows it is the same text, and say so precisely.
Record identity exactly as seen; record host kind and licence evidence; version, full body and size are "unknown" unless a record states them; a preview or table of contents is not a full body.
Write ${D}/out-${s}.jsonl, one line per entry: {"acq_id","key","identity_corrected":"<exact citation as established, or same>","state":"candidate|still_none","candidate":{"url","host","host_kind","identity_seen","version_match":"exact|different:<what>|unknown","full_body":"yes|no|unknown","size","evidence_urls":[...]},"search_log":[queries/sites tried]}. Return counts.`,
    { model: 'opus', effort: 'high', schema: SC, label: `scout3:${s}`, phase: 'Scout' }),
  (sc, s) => (!sc || !sc.candidates) ? { checked: 0, confirmed: 0, rejected: 0 } : run(`${COMMON}
TASK: independently verify every "candidate" line in ${D}/out-${s}.jsonl (you have not seen how they were found). For each: WebFetch the candidate url and evidence; confirm it identifies the required work (authors, title, container, year), the version matches the required version (or state exactly how it differs), the link leads to the full body (not abstract/preview), the host is not a shadow library or borrow-only lending, and note stated size/pages. Write ${D}/out-${s}.verified.jsonl: the same lines plus "verification":{"identity":"confirmed|rejected|unresolved","version_match":"exact|different:<what>|unknown","full_body":"yes|no|unknown","notes":"..."}. Return counts.`,
    { model: 'opus', effort: 'high', schema: VE, label: `verify3:${s}`, phase: 'Verify' }).then(v => ({ shard: s, scout: sc, verify: v })))
const ok = out.filter(Boolean)
return { shards: ok.length, candidates: ok.reduce((n, r) => n + ((r.scout && r.scout.candidates) || 0), 0),
  still_none: ok.reduce((n, r) => n + ((r.scout && r.scout.still_none) || 0), 0),
  confirmed: ok.reduce((n, r) => n + ((r.verify && r.verify.confirmed) || 0), 0) }