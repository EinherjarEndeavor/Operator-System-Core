$statePath = "C:\Users\Tarot\Operator\Control\build-state.json"
$backupPath = "C:\Users\Tarot\Operator\Control\BrainArchive\pre-build\build-state-pre-repair.json"

$current = Get-Content $statePath -Raw
[System.IO.File]::WriteAllText($backupPath, $current, [System.Text.Encoding]::UTF8)
Write-Host "[BACKUP] build-state.json → pre-repair backup"

$state = $current | ConvertFrom-Json

if ($null -eq $state.phases) {
    $state | Add-Member -MemberType NoteProperty -Name "phases" -Value @{}
}
if ($null -eq $state.phases.phase_4_mcp) {
    $state.phases | Add-Member -MemberType NoteProperty -Name "phase_4_mcp" -Value @{}
}
if ($null -eq $state.phases.phase_5_gemini_md) {
    $state.phases | Add-Member -MemberType NoteProperty -Name "phase_5_gemini_md" -Value @{}
}
if ($null -eq $state.session_log) {
    $state | Add-Member -MemberType NoteProperty -Name "session_log" -Value @()
}

$state.phases.phase_4_mcp.status = "COMPLETE"
$state.phases.phase_4_mcp.completed_at = (Get-Date -Format "yyyy-MM-ddTHH:mm:ssZ")
$state.phases.phase_4_mcp.servers_configured = @(
  "operator-filesystem","sqlite-rve","sqlite-lifestate","sqlite-arsenal",
  "sqlite-everything","sqlite-settings","obsidian","notion","github"
)

$state.phases.phase_5_gemini_md.status = "COMPLETE"
$state.phases.phase_5_gemini_md.completed_at = (Get-Date -Format "yyyy-MM-ddTHH:mm:ssZ")
$state.phases.phase_5_gemini_md.sections_written = @(
  "SECTION_1_ARCHITECTURE_MAP","SECTION_2_WRITE_DOCTRINE",
  "SECTION_3_MEMORY_TIER_MAP","SECTION_4_SESSION_PROTOCOL",
  "SECTION_5_PERSONA_ANCHOR","SECTION_6_COGNITIVE_ARCH_INDEX"
)

$state.next_phase = "phase_6_skills"
$state.last_updated = (Get-Date -Format "yyyy-MM-ddTHH:mm:ssZ")

$newEntry = [PSCustomObject]@{
  session = 6
  prompt = "Repair + Phase 5 - settings.json + settings.db + GEMINI.md"
  phases_completed = @("repair_r1","repair_r2","repair_r3","phase_5_gemini_md")
  timestamp = (Get-Date -Format "yyyy-MM-ddTHH:mm:ssZ")
}

$state.session_log += $newEntry

$json = $state | ConvertTo-Json -Depth 20
[System.IO.File]::WriteAllText($statePath, $json, [System.Text.Encoding]::UTF8)
Write-Host "[WRITE] build-state.json - next_phase: phase_6_skills"

