$ErrorActionPreference = 'Stop'
$taskRepo = 'C:\Dev\the-methods-of-reason'
foreach ($taskRel in @('handbook/parts/p06/cardinal-characteristics-and-inequalities.tex','handbook/annex/p06/cardinal-characteristics-and-inequalities.tex')) {
    $taskPath = Join-Path $taskRepo $taskRel
    $taskLines = @(Get-Content -LiteralPath $taskPath)
    $taskPatch = [System.Collections.Generic.List[string]]::new()
    $taskPatch.Add('*** Begin Patch')
    $taskPatch.Add('*** Update File: ' + $taskPath.Replace('\','/'))
    $taskChanged = 0
    foreach ($taskLine in $taskLines) {
        $taskNew = $taskLine.Replace('\mathcal I_{\mathrm{null}}','\mathcal N').Replace('\mathcal I_{\mathrm{meager}}','\mathcal M')
        if ($taskNew -ne $taskLine) {
            $taskPatch.Add('@@')
            $taskPatch.Add('-' + $taskLine)
            $taskPatch.Add('+' + $taskNew)
            $taskChanged++
        }
    }
    $taskPatch.Add('*** End Patch')
    if (-not $taskChanged) { throw "No source-glyph occurrences in $taskRel" }
    $taskKind = $(if ($taskRel -match '/parts/') { 'body' } else { 'annex' })
    [pscustomobject]@{target=$taskRel;kind=$taskKind;changed_lines=$taskChanged;patch_text=($taskPatch -join "`n");source_sha256=(Get-FileHash -LiteralPath $taskPath -Algorithm SHA256).Hash}
}
