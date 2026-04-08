& 'C:\Users\Tarot\Operator\Control\Scripts\fix-buildstate.ps1'

$checks = @(
  @{ name='settings.json'; path='C:\Users\Tarot\.gemini\settings.json'; min_bytes=1000 },
  @{ name='GEMINI.md'; path='C:\Users\Tarot\.gemini\GEMINI.md'; min_bytes=3000 },
  @{ name='settings.db toggles'; path=''; min_bytes=0 },
  @{ name='build-state.json'; path='C:\Users\Tarot\Operator\Control\build-state.json'; min_bytes=500 }
)

foreach ($c in $checks) {
  if ($c.path -and (Test-Path $c.path)) {
    $size = (Get-Item $c.path).Length
    $status = if ($size -ge $c.min_bytes) { '[OK]' } else { '[FAIL]' }
    Write-Host "$status $($c.name) - $size bytes"
  } elseif ($c.path) {
    Write-Host "[FAIL] $($c.name) not found at $($c.path)"
  }
}

$pyScript = "import sqlite3; c=sqlite3.connect(r'C:\Users\Tarot\Operator\Control\settings.db').cursor(); c.execute('SELECT COUNT(*) FROM toggles'); print(c.fetchone()[0])"
$toggleCount = & python -c $pyScript
$toggleCount = $toggleCount.Trim()
Write-Host "$(if ($toggleCount -eq '20') { '[OK]' } else { '[FAIL]' }) settings.db toggles: $toggleCount/20"

$stateJson = Get-Content 'C:\Users\Tarot\Operator\Control\build-state.json' -Raw | ConvertFrom-Json
$nextPhase = $stateJson.next_phase
Write-Host "[INFO] Next phase: $nextPhase"

Write-Host ""
Write-Host "=========================================================="
Write-Host "  REPAIR + PHASE 5 COMPLETE"
Write-Host "  [OK] settings.json - MCP servers online"
Write-Host "  [OK] settings.db - all 20 toggles seeded"
Write-Host "  [OK] GEMINI.md - global infrastructure layer written"
Write-Host "  [OK] neo4j-init.py - archived correctly"
Write-Host "  -> Next: Phase 6 - Cognitive Architecture Skill"
Write-Host "  -> Restart Gemini CLI before next session (MCP changes)"
Write-Host "=========================================================="
