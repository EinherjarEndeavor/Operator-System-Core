# install.ps1 
Write-Host "[RVE] Starting installation..." -ForegroundColor Cyan 
$folders = @("rve/data", "rve/scripts", "rve/templates", "rve/config", "rve/exports", "rve/logs") 
foreach ($folder in $folders) { 
    if (-not (Test-Path $folder)) { New-Item -ItemType Directory -Path $folder -Force | Out-Null } 
} 
python rve/scripts/setup.py 
Write-Host "[RVE] Installation complete!" -ForegroundColor Cyan
