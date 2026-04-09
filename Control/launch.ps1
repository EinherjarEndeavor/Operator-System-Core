# Load .env into session environment
Get-Content "C:\Users\Tarot\Operator\.env" | ForEach-Object {
    if ($_ -match '^\s*([^#][^=]*?)\s*=\s*(.*)\s*$') {
        [System.Environment]::SetEnvironmentVariable($matches[1].Trim(), $matches[2].Trim(), 'Process')
    }
}

Set-Location C:\Users\Tarot\Operator
Write-Host "RVE | tar0t | $(Get-Date -Format 'ddd HH:mm')" -ForegroundColor Cyan
Write-Host "ENV loaded | Neo4j: $($env:NEO4J_URI)" -ForegroundColor DarkGray
gemini
