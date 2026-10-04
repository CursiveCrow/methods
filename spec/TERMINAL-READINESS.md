# Terminal readiness

`tools/check_terminal_readiness.py` first streams the complete inherited source
map and validates every discovered exact restoration/provenance record. A map
interval counts as accounted only when cited restoration locators cover every
one of its physical lines exactly once; an absent range or a duplicate range,
including a second claim on the preserved `9099--9111` island, stays OPEN. The
checker also invokes the source-order checker in its terminal form:

```text
python tools/check.py --tree handbook --strict --require-no-pending-inherited-refs
```

Its `inherited_source_order` gate pins a deterministic digest of the complete
handbook TeX tree and remains OPEN for every governed pending inherited
reference. The checker then checks the generated source-unit, handbook-unit,
register-obligation, acquisition-gap, and packet-admission ledgers before
aggregating them. It streams the full external-coverage manifest against the
indexed assignment sidecars, validates the one-book publication controls, and
writes or checks
`spec/verification/terminal-readiness-manifest.json`.

For every reviewed-record ledger, the terminal row and each of these six
separate gates must pass:

1. `source_fidelity_ai`
2. `topic_specialist_ai`
3. `adversarial_publication_ai`
4. `static`
5. `build`
6. `visual`

For the register-obligation gate, `COMPLETE` and
`SUPERSEDED_BY_CONTRACT` are the only terminal dispositions. The latter never
means completion: it applies only to the generator-validated atomic notation
contract record. It counts only after
`tools/build_register_obligation_closure.py --check` reproduces the committed
CSV and all six review columns pass, so manually editing the CSV cannot advance
terminal readiness.

The generated readiness manifest deliberately does not claim that the user has
accepted the book. While any non-user residual remains, the
`user_final_acceptance` gate is `absent` and an acceptance file is rejected.
When all other residuals reach zero, the generated manifest changes only to
`pending` acceptance. The user may then supply
`spec/provenance/user-final-acceptance.json`, conforming to its schema and
pinning the exact readiness-manifest digest plus the exact title, path, hash,
byte count, and page count of the final public PDF. The publication manifest's
release object must in turn pin both files and the same PDF hash. This ordering
avoids a digest cycle and prevents either record from setting its own approval.

Current readiness is checked with:

```text
python tools/check_terminal_readiness.py --check
```

The final release gate additionally requires:

```text
python tools/check_terminal_readiness.py --check --require-ready
```

## Why this administrative record exists

- **Necessity:** separate valid ledgers cannot state that every independent
  residual is simultaneously zero for one exact public PDF.
- **Definition:** the terminal-readiness manifest is the deterministic
  metalinguistic aggregate of the exact gate counts, ledger digests, review-gate
  counts, external assignment totals, and public-PDF identity checked in one
  run.
- **Standing:** it is an administrative release record, not a motive, logical
  relation, statement family, or source-content claim.
- **Nonredundancy:** upstream ledgers decide individual admissions and
  assignments; this record only joins their terminal counts and immutable
  artifact identities, while the separate user record alone supplies final
  acceptance.
- **Use:** the one-book publication manifest may enter release state only when
  `--require-ready` validates this exact zero-residual manifest, the user's
  acceptance record, and all reciprocal release hashes.
