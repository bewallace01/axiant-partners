param(
    [string]$PostPath,
    [switch]$All
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

function Get-Category([string]$name) {
    $n = $name.ToLower()
    if ($n -match "sba") { return "sba" }
    if ($n -match "equipment") { return "equipment" }
    if ($n -match "line-of-credit") { return "linecredit" }
    if ($n -match "term-loan") { return "termloan" }
    if ($n -match "working-capital") { return "workingcapital" }
    if ($n -match "commercial-bridge") { return "bridge" }
    if ($n -match "commercial-real-estate|commercial-property") { return "cre" }
    if ($n -match "fix-and-flip") { return "fixflip" }
    if ($n -match "revenue-based|merchant-cash-advance") { return "revenue" }
    if ($n -match "securities-based") { return "securities" }
    return "general"
}

function Get-Root {
    return (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
}

function Read-Text([string]$path) {
    return [System.IO.File]::ReadAllText($path)
}

function Write-Text([string]$path, [string]$content) {
    $utf8NoBom = [System.Text.UTF8Encoding]::new($false)
    [System.IO.File]::WriteAllText($path, $content, $utf8NoBom)
}

function Get-Title([string]$content) {
    return [regex]::Match($content, "<title>(.*?)</title>", "IgnoreCase,Singleline").Groups[1].Value
}

function Get-Description([string]$content) {
    return [regex]::Match($content, "<meta\s+name=""description""\s+content=""(.*?)""\s*/?>", "IgnoreCase,Singleline").Groups[1].Value
}

function Get-H1([string]$content) {
    $h1 = [regex]::Match($content, "<h1[^>]*>(.*?)</h1>", "IgnoreCase,Singleline").Groups[1].Value
    $h1 = [regex]::Replace($h1, "<[^>]+>", "")
    return [System.Net.WebUtility]::HtmlDecode($h1).Trim()
}

function Ensure-OpenGraphAndTwitter([string]$content) {
    $title = Get-Title $content
    $desc = Get-Description $content
    if (-not $title -or -not $desc) {
        throw "Missing <title> or meta description."
    }

    $safeTitle = $title -replace "&", "&amp;"
    $safeDesc = $desc -replace "&", "&amp;"

    if ([regex]::IsMatch($content, "<meta\s+property=""og:title""", "IgnoreCase")) {
        $content = [regex]::Replace($content, "<meta\s+property=""og:title""\s+content="".*?""\s*/?>", "<meta property=""og:title"" content=""$safeTitle"">", "IgnoreCase,Singleline")
    }
    if ([regex]::IsMatch($content, "<meta\s+property=""og:description""", "IgnoreCase")) {
        $content = [regex]::Replace($content, "<meta\s+property=""og:description""\s+content="".*?""\s*/?>", "<meta property=""og:description"" content=""$safeDesc"">", "IgnoreCase,Singleline")
    }

    $twCard = '<meta name="twitter:card" content="summary_large_image">'
    $twTitle = '<meta name="twitter:title" content="' + $safeTitle + '">'
    $twDesc = '<meta name="twitter:description" content="' + $safeDesc + '">'

    if ([regex]::IsMatch($content, "<meta\s+name=""twitter:card""", "IgnoreCase")) {
        $content = [regex]::Replace($content, "<meta\s+name=""twitter:card""\s+content="".*?""\s*/?>", $twCard, "IgnoreCase,Singleline")
    } elseif ([regex]::IsMatch($content, "(<meta\s+property=""og:site_name""\s+content="".*?""\s*/?>)", "IgnoreCase,Singleline")) {
        $content = [regex]::Replace($content, "(<meta\s+property=""og:site_name""\s+content="".*?""\s*/?>)", "`$1`r`n    $twCard", "IgnoreCase,Singleline")
    } elseif ([regex]::IsMatch($content, "(<meta\s+property=""og:image""\s+content="".*?""\s*/?>)", "IgnoreCase,Singleline")) {
        $content = [regex]::Replace($content, "(<meta\s+property=""og:image""\s+content="".*?""\s*/?>)", "`$1`r`n    $twCard", "IgnoreCase,Singleline")
    }

    if ([regex]::IsMatch($content, "<meta\s+name=""twitter:title""", "IgnoreCase")) {
        $content = [regex]::Replace($content, "<meta\s+name=""twitter:title""\s+content="".*?""\s*/?>", $twTitle, "IgnoreCase,Singleline")
    } else {
        $content = [regex]::Replace($content, "(<meta\s+name=""twitter:card""\s+content="".*?""\s*/?>)", "`$1`r`n    $twTitle", "IgnoreCase,Singleline")
    }

    if ([regex]::IsMatch($content, "<meta\s+name=""twitter:description""", "IgnoreCase")) {
        $content = [regex]::Replace($content, "<meta\s+name=""twitter:description""\s+content="".*?""\s*/?>", $twDesc, "IgnoreCase,Singleline")
    } else {
        $content = [regex]::Replace($content, "(<meta\s+name=""twitter:title""\s+content="".*?""\s*/?>)", "`$1`r`n    $twDesc", "IgnoreCase,Singleline")
    }

    return $content
}

function Normalize-TextArtifacts([string]$content) {
    $content = [regex]::Replace($content, "(<p class=""blog-back""><a [^>]*>)\s*<-\s*Back to\s*", '$1&larr; Back to ', "IgnoreCase,Singleline")
    $content = [regex]::Replace($content, "(<p class=""blog-byline"">)([^<]*?)(</p>)", {
        param($m)
        $txt = $m.Groups[2].Value
        $txt = [regex]::Replace($txt, "\s+-\s+", " - ")
        return $m.Groups[1].Value + $txt.Trim() + $m.Groups[3].Value
    }, "IgnoreCase,Singleline")
    return $content
}

function Ensure-RelatedResources(
    [string]$content,
    [string]$fileName,
    [hashtable]$catMap,
    [hashtable]$titleMap,
    [string[]]$allNames
) {
    $hubMap = @{
        sba            = "../../"
        equipment      = "../../"
        linecredit     = "../../"
        termloan       = "../../"
        workingcapital = "../../"
        bridge         = "../../"
        cre            = "../../"
        fixflip        = "../../"
        revenue        = "../../"
        securities     = "../../"
        general        = "../../../blog.html"
    }
    $hubLabel = @{
        sba            = "SBA Loans Blog"
        equipment      = "Equipment Financing Blog"
        linecredit     = "Business Line of Credit Blog"
        termloan       = "Business Term Loans Blog"
        workingcapital = "Working Capital Loans Blog"
        bridge         = "Commercial Bridge Loans Blog"
        cre            = "Commercial Real Estate Loans Blog"
        fixflip        = "Fix and Flip Blog"
        revenue        = "Revenue-Based Financing Blog"
        securities     = "Securities-Based Lending Blog"
        general        = "Blog Hub"
    }
    $serviceMap = @{
        sba            = "../sba-loans.html"
        equipment      = "../equipment-financing.html"
        linecredit     = "../business-line-of-credit.html"
        termloan       = "../business-term-loans.html"
        workingcapital = "../working-capital-loans.html"
        bridge         = "../commercial-bridge-loans.html"
        cre            = "../commercial-real-estate-loans.html"
        fixflip        = "../fix-and-flip.html"
        revenue        = "../revenue-based-financing.html"
        securities     = "../securities-based-lending.html"
        general        = "../services.html"
    }
    $serviceLabel = @{
        sba            = "SBA loan options"
        equipment      = "equipment financing options"
        linecredit     = "business line of credit options"
        termloan       = "business term loan options"
        workingcapital = "working capital loan options"
        bridge         = "commercial bridge loan options"
        cre            = "commercial real estate loan options"
        fixflip        = "fix and flip loan options"
        revenue        = "revenue-based financing options"
        securities     = "securities-based lending options"
        general        = "business financing options"
    }

    $cat = $catMap[$fileName]
    $relatedName = ($allNames | Where-Object { $_ -ne $fileName -and $catMap[$_] -eq $cat } | Select-Object -First 1)
    if ($relatedName) {
        $relatedHref = "./$relatedName"
        $relatedTitle = $titleMap[$relatedName]
    } else {
        $relatedHref = $hubMap[$cat]
        $relatedTitle = "Browse all business financing articles"
    }

    $block = @"
            <section class="related-resources" aria-label="Related resources">
                <h2>Related Resources</h2>
                <ul>
                    <li><a href="$($serviceMap[$cat])">Explore $($serviceLabel[$cat])</a></li>
                    <li><a href="$($hubMap[$cat])">Read more in the $($hubLabel[$cat])</a></li>
                    <li><a href="$relatedHref">Related article: $relatedTitle</a></li>
                    <li><a href="../match.html">Get matched with lenders</a></li>
                </ul>
            </section>

"@

    $content = [regex]::Replace($content, "\s*<section class=""related-resources""[\s\S]*?</section>\s*", "`r`n`r`n", "IgnoreCase")
    $content = [regex]::Replace($content, "\s*<div class=""services-cta"">", "`r`n`r`n$block            <div class=""services-cta"">", "IgnoreCase")
    return $content
}

$root = Get-Root
$blogDir = Join-Path $root "blog"
if (-not (Test-Path $blogDir)) {
    throw "Could not find blog directory at $blogDir"
}

$allFiles = Get-ChildItem -Path $blogDir -Filter "*.html" | Sort-Object Name
if ($allFiles.Count -eq 0) {
    throw "No blog HTML files found."
}

$targets = @()
if ($All) {
    $targets = $allFiles
} elseif ($PostPath) {
    $resolved = Resolve-Path (Join-Path $root $PostPath) -ErrorAction Stop
    $fileName = [System.IO.Path]::GetFileName($resolved.Path)
    $match = $allFiles | Where-Object { $_.Name -eq $fileName } | Select-Object -First 1
    if (-not $match) {
        throw "PostPath must point to a file inside blog/: $PostPath"
    }
    $targets = @($match)
} else {
    throw "Provide -PostPath blog/<file>.html or use -All."
}

$titleMap = @{}
$catMap = @{}
foreach ($file in $allFiles) {
    $content = Read-Text $file.FullName
    $titleMap[$file.Name] = Get-H1 $content
    $catMap[$file.Name] = Get-Category $file.Name
}

$updated = 0
foreach ($file in $targets) {
    $content = Read-Text $file.FullName
    $next = $content
    $next = Ensure-OpenGraphAndTwitter $next
    $next = Normalize-TextArtifacts $next
    $next = Ensure-RelatedResources -content $next -fileName $file.Name -catMap $catMap -titleMap $titleMap -allNames ($allFiles.Name)

    if ($next -ne $content) {
        Write-Text -path $file.FullName -content $next
        $updated++
        Write-Output "Updated: $($file.Name)"
    } else {
        Write-Output "No changes: $($file.Name)"
    }
}

Write-Output "Done. Updated $updated file(s)."
