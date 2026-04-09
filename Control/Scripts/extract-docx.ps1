param([string]$path)
Add-Type -AssemblyName System.IO.Compression.FileSystem
$tempDir = [System.IO.Path]::Combine([System.IO.Path]::GetTempPath(), [System.Guid]::NewGuid().ToString())
[System.IO.Compression.ZipFile]::ExtractToDirectory($path, $tempDir)
$xmlPath = [System.IO.Path]::Combine($tempDir, "word", "document.xml")
if (Test-Path $xmlPath) {
    [xml]$xml = Get-Content $xmlPath
    $ns = New-Object System.Xml.XmlNamespaceManager($xml.NameTable)
    $ns.AddNamespace("w", "http://schemas.openxmlformats.org/wordprocessingml/2006/main")
    $text = $xml.SelectNodes("//w:t", $ns) | ForEach-Object { $_.InnerText }
    $text -join " "
}
Remove-Item $tempDir -Recurse -Force
