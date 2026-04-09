param(
    [string]$FolderPath = "C:\Users\tarot\Operator",
    [string]$RepoName = "Operator",
    [string]$GitHubOwner = "EinherjarEndeavor",
    [string]$DefaultBranch = "main",
    [string]$Visibility = "private"
)

$ErrorActionPreference = "Stop"

if (!(Test-Path $FolderPath)) {
    throw "Folder not found: $FolderPath"
}

Set-Location $FolderPath

if (!(Test-Path ".git")) {
    git init
}

git add .

try {
    git commit -m "Initial commit"
} catch {
    Write-Host "Nothing to commit yet, continuing..."
}

# Requires GitHub CLI
$repoExists = $false
try {
    gh repo view "$GitHubOwner/$RepoName" | Out-Null
    $repoExists = $true
} catch {
    $repoExists = $false
}

if (-not $repoExists) {
    if ($Visibility -eq "public") {
        gh repo create "$GitHubOwner/$RepoName" --source . --remote origin --push --public
    } else {
        gh repo create "$GitHubOwner/$RepoName" --source . --remote origin --push --private
    }
} else {
    Write-Host "Repo already exists. Configuring remote and pushing..."
    $remoteUrl = "https://github.com/$GitHubOwner/$RepoName.git"

    $hasOrigin = $false
    try {
        git remote get-url origin | Out-Null
        $hasOrigin = $true
    } catch {
        $hasOrigin = $false
    }

    if ($hasOrigin) {
        git remote set-url origin $remoteUrl
    } else {
        git remote add origin $remoteUrl
    }

    git branch -M $DefaultBranch
    git push -u origin $DefaultBranch
}

Write-Host "Done: https://github.com/$GitHubOwner/$RepoName"