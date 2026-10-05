export const meta = {
  name: 'tmor-upgrade-audit',
  description: 'Fresh adversarial Opus audit of a 1-in-20 sample of a wave\'s authored_unreviewed rows',
  phases: [{ title: 'Audit', detail: 'one fresh Opus auditor per sampled section', model: 'opus' }],
}
const DIR = `spec/coverage/edition-2026/assessments/${args.wave}`
const SCHEMA = { type: 'object', properties: {
  section_id: { type: 'string' }, all_covered: { type: 'boolean' },
  failures: { type: 'array', items: { type: 'object', properties: { key: { type: 'string' }, verdict: { type: 'string' }, gap: { type: 'string' } }, required: ['key', 'verdict', 'gap'] } },
  assessment_id: { type: 'string' } }, required: ['section_id', 'all_covered', 'failures', 'assessment_id'] }
const prompt = s => `READ-ONLY adversarial coverage AUDIT (fresh context, role "audit"). Repository C:/Dev/the-methods-of-reason (Windows; Git Bash). You may write ONLY the one assessment file named below.
Section ${s.section} "${s.title}" is recorded as authored_unreviewed: two earlier assessors judged every owed item covered. Your job is to find out whether that is wrong. Default to NOT covered when the text does not plainly meet a success condition.
Owed components (each queue unit's required_components in spec/coverage/edition-2026/completion-work-queue.jsonl, units ${s.units.join(', ')}; read each component's description, success_condition and failure_condition there): ${s.components ? s.components.join(', ') : 'EVERY required component of those units (list them all from the queue file)'}. The packet ${s.packet} lists related hosts and files; find the treatment on the handbook route yourself (handbook/main.tex and the \\input tree; grep labels and titles).
Rules: you assess coverage only (is each component present in complete form at cited lines), not correctness, and you admit nothing. "covered" needs every element of the success_condition present at lines you cite and no failure_condition holding. A proof counts only if its steps are written; "standard", "similarly", a citation in place of an owed proof, or a sketch means partial. A source-specific component needs the held source (spec/coverage/edition-2026/held-sources.json; source/formal-logic-reference.tex is the held FLRV1 Version 1.0) opened at two cited locators. Do not open spec/research/*, *-return.json files, ledger prose or other assessment files.
Write ${DIR}/CA-${args.wave}-${s.section}-audit.json: {"schema":"coverage-assessment/1","assessment_id":"CA-${args.wave}-${s.section}-audit","section_id":"${s.section}","assessor":{"family":"anthropic","model":"opus","role":"audit","context_id":"${args.wave}-${s.section}-audit"},"inputs":{"tex":[{"path","sha256"}],"sources_opened":[{"path","sha256","pages"}]},"components":[exactly one {"component_id","verdict","evidence":[{"path","line_start","line_end","label"}],"gap"} per owed component],"duties":[],"defect_observations":[...]}.
Return section_id, all_covered (true only if every owed component is covered), failures (each non-covered key with verdict and the gap in the success condition's own terms) and assessment_id.`
phase('Audit')
const res = await parallel(args.sample.map(s => () => agent(prompt(s), { model: 'opus', effort: 'max', schema: SCHEMA, label: `audit:${s.section}`, phase: 'Audit' })))
return { wave: args.wave, results: res }