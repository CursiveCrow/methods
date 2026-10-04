$ErrorActionPreference = 'Stop'
$taskRepo = 'C:\Dev\the-methods-of-reason'
foreach ($taskRel in @('handbook/parts/p08/mckinsey-tarski-topological-completeness.tex','handbook/annex/p08/mckinsey-tarski-topological-completeness.tex')) {
    $taskPath = Join-Path $taskRepo $taskRel
    $taskPatch = [System.Collections.Generic.List[string]]::new()
    $taskPatch.Add('*** Begin Patch')
    $taskPatch.Add('*** Update File: ' + $taskPath.Replace('\','/'))
    $taskCount = 0
    foreach ($taskLine in Get-Content -LiteralPath $taskPath) {
        $taskNew = $taskLine.Replace('lem:p08-mt-','thm:p08-mt-')
        if ($taskNew -ne $taskLine) {
            $taskPatch.Add('@@'); $taskPatch.Add('-' + $taskLine); $taskPatch.Add('+' + $taskNew); $taskCount++
        }
    }
    $taskPatch.Add('*** End Patch')
    if (-not $taskCount) { throw 'No label repair needed in target' }
    [pscustomobject]@{target=$taskRel;changed_lines=$taskCount;patch_text=($taskPatch -join "`n")}
}
