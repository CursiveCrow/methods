# C6 publication finding: notation-note TeX repair

Date: 7 September 2026. All three independent first-round C6 reviews have
filed. The manuscript passed their mathematical, source and publication-text
scopes. The publication review failed the candidate apparatus because the new
rho row's prose contained an unprotected underscore.

Root checked all canonical note cells after removing their inline math spans.
Exactly six notes contained unescaped prose underscores, at CSV lines 864,
865, 866, 868, 870 and 873. The first five were earlier C5 notes; the last
was the C6 finding. This is a focused syntax check, not a full TeX parser.

All six now use the intended inline mathematical notation: Z_phi, z_a,
r_epsilon, S_phi and n_0/n_1/n_2 use the actual manuscript glyphs, and
code_5 uses the operator form. Roles, scopes, row identities and all manuscript
files are unchanged. No unrelated registry row changed. The existing tool
regenerated isolated C6 candidates; active views were not promoted.

| Artifact | Before SHA256 | After SHA256 |
| --- | --- | --- |
| handbook/registry/symbols.csv | 54F108553D5B719EB06BC3B85808656D4AF5BF56397ADF4643EB10C57D8B0D79 | F8E907A8322C9584AAB6A8ED59FC25AE5200EE4FBE941AA77ED20AC58226EFDE |
| tmp/edition-2026-c6-candidate/symbols-tables.tex | 79E2C62BAF9D5E566AFA251ABF6A2F3E4BAE2F83C1481F1BCF25821D28328712 | 6D2166E7EA09A6DEB9682B2275008255832AB0D0BE5DC6886F3359EE33B6C19D |
| tmp/edition-2026-c6-candidate/symbol-index.tex | 03231E48997471D9EF625A7584CB54AD85ED7F5F822338125BF39AA78B0CBCD5 | 3D1753BA052288216F8EF32E7F11B6CEC9DD1BC55C255F10C5B985355C984B0D |

The 886-row field/scope/exact-glyph checks pass. The repeated focused
prose-underscore search returns no rows. Independent publication recheck
must cover all six notes and both candidate representations. Older C5
projections remain historical construction evidence; their former note
encoding is not a current publication pass.

No proof edit, software test, build, render, provenance admission or active
view promotion was part of this repair.
