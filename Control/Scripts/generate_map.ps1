$root = "C:\Users\tarot\Operator"
Get-ChildItem -Path $root -Recurse | Select-Object `
    @{Name='FullName';Expression={$_.FullName}}, `
    @{Name='Size(KB)';Expression={[math]::Round($_.Length / 1KB, 2)}} | `
    Format-Table -AutoSize | Out-String | Set-Content -Path "$root\file_list_detailed.txt"
