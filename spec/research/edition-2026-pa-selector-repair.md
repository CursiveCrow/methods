# Exact seven-axiom selector repair

Date: 7 September 2026 local time. Finding SF-A1 from the independent
`spec/verification/edition-2026-pa-abduction-source-review.md`, SHA256
`45c2d6352e4afd90cdeb0a90ff264ab76d921b0fdd2996b3e63f616b89fcc4e9`.

The reviewed P5 body used a bounded sum with the expression q_(j+1), where
the seven q constants were literal constructor expressions. Its description
language compiles bounded sums as primitive recursion. Without a specified
counter selector and total default, that notation did not fix one formation
tree and therefore did not select the claimed exact arithmetic graph.

The active definition now specifies Q_7 as the exact seven-entry cons-list
of q_1 through q_7, and evaluates e(Q_7,j) using the already declared total
entry description. That entry has value zero outside positions zero through
six. The bounded sum retains the declared fold expansion and now has a
particular fully specified selector. The displayed definitions use two
aligned rows. No test program or source convention was introduced.

The repaired body has SHA256
`ec93120e394dac60169efabce50cb174c44ad65502674f9e704c8adf6efa92d2`.
The preceding reviewed body hash was
`33195dff4bb6d2d7bd898e0af9d8ec1980a1272593139624aa17577e132c15f5`.
The annex is unchanged at
`03baf39d646901dc307812b0d22fe8823cfec53b3d7b85a3ff0adf754aaf71e5`.
All finite-abduction text, sources and integration routes are unchanged.

One Q_7/entry-selector row was appended to the notation registry, now 981
rows with SHA256
`f903fad8c3a59673ad805f26960b9bfdb2d115a25291603bf0db1c0feb7868c4`.
The existing generator passed with the new row and regenerated only isolated
candidate views. Their hashes are
`7ee781be32cb81f8117e52d49922434610dacdf8838ed019498dba1bff8d203a`
for symbols-tables.tex and
`c533c752cdc0669bd33a30b2d639db5bc73d38d899953b869cd4d3111e1f0326`
for symbol-index.tex, both under tmp/edition-2026-p5-p16-integration/.

The original source reviewer has received this frozen repair for a focused
independent recheck. This note records the edit, not a self-issued PASS.
Topic/publication reviews and all remaining admission gates are still due.
The separate D3, predicate-consumer and GL obligations remain open.
