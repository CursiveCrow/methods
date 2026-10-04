# Open TeX build defects

## 1. TeX main memory exhausted on the second pdflatex pass (forbidden file: tools/texlive.latexmkrc)

- Symptom: with the binding command and default TeX Live 2025 memory,
  pass 1 completes (no errors), but every later pass dies with
  `./generated/audit-p06.tex:169: TeX capacity exceeded, sorry [main memory size=5000000]`
  (`5000000 words of memory out of 5000000`), no PDF. Reproduced in
  run-6 (latexmk pass 2) and run-9 (single pdflatex pass over the
  complete run-8 aux, 25 s to failure).
- Cause: capacity, not syntax. Pass 1 peaks at ~2.4M words; from pass 2
  the ~30,800 `\newlabel` definitions (~3.3 MB of main.aux) are loaded as
  token lists, pushing the peak to ~5.36M words (run-8 reports
  `10360557 words of memory out of 14933256` with 5,000,000 of that
  being the extra_mem_bot reservation).
- Exact needed fix: add these two lines at the top of
  `tools/texlive.latexmkrc` (latexmk passes `%ENV` to pdflatex; kpathsea
  reads both variables at run time, no format rebuild needed; verified
  with a scratch copy of the rc):

      $ENV{'extra_mem_top'} = '10000000';
      $ENV{'extra_mem_bot'} = '5000000';

- With exactly these values exported in the environment (run-8), the full
  latexmk build completes: exit 0, `All targets (main.pdf) are up-to-date`,
  9605 pages.

No other unfixed defects: the run-8 final pass has zero TeX errors.
