$envContent = Get-Content "C:\Users\Tarot\Operator\.env" -Raw
$notionKeyLine = $envContent -split "`n" | Where-Object { $_ -match "^NOTION_API_KEY=" }
if ($null -eq $notionKeyLine) {
    Write-Host "[FAIL] NOTION_API_KEY not found in .env"
    exit 1
}
$notionKey = ($notionKeyLine -split "=",2)[1].Trim()

# Build MCP Headers for Notion
$notionHeaders = @{
    "Authorization" = "Bearer $notionKey"
    "Notion-Version" = "2022-06-28"
}
$notionHeadersJson = $notionHeaders | ConvertTo-Json -Compress

$json = [ordered]@{
    theme = "Default"
    autoAccept = $false
    model = "gemini-2.5-pro"
    contextFileName = "GEMINI.md"
    compressionThreshold = 0.99
    fileFiltering = [ordered]@{
        respectGitignore = $true
        enableDefaultIgnores = $true
    }
    mcpServers = [ordered]@{
        "operator-filesystem" = [ordered]@{
            command = "npx"
            args = @("-y", "@modelcontextprotocol/server-filesystem", "C:\Users\Tarot\Operator")
        }
        "sqlite-rve" = [ordered]@{
            command = "npx"
            args = @("-y", "mcp-sqlite", "C:\Users\Tarot\Operator\Control\rve.db")
        }
        "sqlite-lifestate" = [ordered]@{
            command = "npx"
            args = @("-y", "mcp-sqlite", "C:\Users\Tarot\Operator\Control\lifestate.db")
        }
        "sqlite-arsenal" = [ordered]@{
            command = "npx"
            args = @("-y", "mcp-sqlite", "C:\Users\Tarot\Operator\Control\arsenal.db")
        }
        "sqlite-everything" = [ordered]@{
            command = "npx"
            args = @("-y", "mcp-sqlite", "C:\Users\Tarot\Operator\Control\everything.db")
        }
        "sqlite-settings" = [ordered]@{
            command = "npx"
            args = @("-y", "mcp-sqlite", "C:\Users\Tarot\Operator\Control\settings.db")
        }
        "obsidian" = [ordered]@{
            command = "npx"
            args = @("-y", "mcp-obsidian", "C:\Users\Tarot\Operator\Vault")
        }
        "notion" = [ordered]@{
            command = "npx"
            args = @("-y", "@notionhq/notion-mcp-server")
            env = @{
                OPENAPI_MCP_HEADERS = $notionHeadersJson
            }
        }
        "github" = [ordered]@{
            command = "npx"
            args = @("-y", "@modelcontextprotocol/server-github")
            env = @{
                GITHUB_PERSONAL_ACCESS_TOKEN = "GITHUB_PAT_HERE"
            }
        }
    }
}

$output = $json | ConvertTo-Json -Depth 10
[System.IO.File]::WriteAllText("C:\Users\Tarot\.gemini\settings.json", $output, [System.Text.Encoding]::UTF8)
$size = (Get-Item "C:\Users\Tarot\.gemini\settings.json").Length
Write-Host "[WRITE] settings.json - $size bytes"
if ($size -lt 500) {
    Write-Host "[FATAL] settings.json too small"
    exit 1
}
Write-Host "[OK] settings.json valid"
