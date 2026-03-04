# Create topic/index.html from topic-blog.html
$hubMap = @{
    "equipment-financing" = "equipment-financing-blog.html"
    "business-line-of-credit" = "business-line-of-credit-blog.html"
    "working-capital-loans" = "working-capital-loans-blog.html"
    "business-term-loans" = "business-term-loans-blog.html"
    "commercial-real-estate-loans" = "commercial-real-estate-loans-blog.html"
    "commercial-bridge-loans" = "commercial-bridge-loans-blog.html"
    "revenue-based-financing" = "revenue-based-financing-blog.html"
    "securities-based-lending" = "securities-based-lending-blog.html"
    "fix-and-flip" = "fix-and-flip-blog.html"
}
$baseDir = Split-Path -Parent $PSScriptRoot
Set-Location $baseDir
foreach ($topic in $hubMap.Keys) {
    $src = $hubMap[$topic]
    $destDir = $topic
    $dest = "$destDir\index.html"
    if (Test-Path $dest) { Write-Host "Exists: $dest"; continue }
    if (-not (Test-Path $src)) { Write-Host "Missing: $src"; continue }
    $c = Get-Content $src -Raw
    $oldUrl = $src -replace '\.html',''   # e.g. equipment-financing-blog
    $c = $c -replace [regex]::Escape("https://www.axiantpartners.com/$oldUrl.html"), "https://www.axiantpartners.com/$topic/"
    $c = $c -replace [regex]::Escape("https://www.axiantpartners.com/$oldUrl"), "https://www.axiantpartners.com/$topic/"
    $c = $c -replace 'href="blog\.html"', 'href="../blog.html"'
    $c = $c -replace 'href="(?!\.\./)([a-z0-9-]+\.html)"', 'href="../$1"'
    $c = $c -replace 'href="blog/([a-z0-9-]+)\.html"', 'href="articles/$1/"'
    # Root assets (styles, images) - add ../
    $c = $c -replace 'href="(?!\.\./|https?://|#)([a-zA-Z0-9_.-]+\.(css|jpg|jpeg|png|svg|ico))"', 'href="../$1"'
    $c = $c -replace 'src="(?!\.\./|https?://|data:)([^"]+)"', 'src="../$1"'
    New-Item -ItemType Directory -Path $destDir -Force | Out-Null
    Set-Content $dest -Value $c -NoNewline
    Write-Host "Created: $dest"
}
