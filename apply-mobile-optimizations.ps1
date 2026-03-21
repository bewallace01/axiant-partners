# Applies mobile optimizations to all HTML files (PowerShell fallback when Node unavailable)
$ErrorActionPreference = "Stop"
$Root = $PSScriptRoot

function Get-HtmlFiles {
    Get-ChildItem -Path $Root -Filter "*.html" -Recurse -File | Where-Object {
        $_.FullName -notmatch "node_modules|\.git"
    } | ForEach-Object { $_.FullName }
}

$criticalCss = (Get-Content "$Root\critical-mobile.css" -Raw).Trim()

$mobileStyle = @"
<style id="mobile-critical">
$criticalCss
</style>

"@

$lazyScript = @'

<script>
if(window.innerWidth<=768){var ls=document.querySelectorAll('.about-section,.testimonials-section,.global-bottom-cta,.site-footer-enhanced,.services-grid,.blog-grid,.steps-grid,.benefits-grid');var so=new IntersectionObserver(function(e){e.forEach(function(entry){if(entry.isIntersecting){entry.target.style.opacity='1';entry.target.style.transform='none';so.unobserve(entry.target);}});},{rootMargin:'100px'});ls.forEach(function(s){s.style.opacity='0';s.style.transition='opacity 0.3s ease';so.observe(s);});}
</script>
'@

$count = 0
Get-HtmlFiles | ForEach-Object {
    $file = $_
    $html = Get-Content $file -Raw
    $orig = $html

    # Step 1: Add mobile-critical style
    if ($html -notmatch 'id="mobile-critical"') {
        $html = $html -replace '(<link[^>]+rel=["'']stylesheet["''][^>]*>)', "$mobileStyle`$1"
    }

    # Step 6: viewport-fit=cover
    if ($html -match 'viewport' -and $html -notmatch 'viewport-fit=cover') {
        $html = $html -replace '<meta\s+name=["'']viewport["''][^>]*>', '<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">'
    }

    # Step 6: theme-color
    if ($html -notmatch 'theme-color') {
        $html = $html -replace '(<head[^>]*>)', "`$1`n<meta name=`"theme-color`" content=`"#0d1f3c`">"
    }

    # Step 6: X-UA-Compatible
    if ($html -notmatch 'X-UA-Compatible') {
        $html = $html -replace '(<head[^>]*>)', "`$1`n<meta http-equiv=`"X-UA-Compatible`" content=`"IE=edge`">"
    }

    # Step 6: dns-prefetch
    if ($html -match 'googletagmanager' -and $html -notmatch 'dns-prefetch') {
        $hints = "`n<link rel=`"dns-prefetch`" href=`"https://fonts.googleapis.com`">`n<link rel=`"dns-prefetch`" href=`"https://fonts.gstatic.com`">`n<link rel=`"dns-prefetch`" href=`"https://www.googletagmanager.com`">"
        $html = $html -replace '(<head[^>]*>)', "`$1$hints"
    }

    # Step 2: For img inside picture - add mobile source as first child; for bare img - wrap
    if ($html -match 'img[^>]+src="[^"]*\/assets\/') {
        # Fix nested picture (our previous run wrapped imgs that were already in picture)
        $html = $html -replace '<picture><source ([^>]+)><picture><source media="\(max-width: 768px\)" srcset="([^"]+)"><img([^>]*)></picture></picture>', '<picture><source media="(max-width: 768px)" srcset="$2"><source $1><img$3></picture>'
        # Wrap bare img (not inside picture) - only if no nested structure remains
        if ($html -notmatch 'picture>.*<picture>') {
            $html = [regex]::Replace($html, '(?<!<source[^>]*>)<img([^>]*?)src="([^"]*\/assets\/[^"]+)"([^>]*)>', {
                param($match)
                $prev = $html.Substring([Math]::Max(0, $match.Index - 100), [Math]::Min(100, $match.Index))
                if ($prev -match '</picture>' -or $prev -match '<source\s') { return $match.Value }
                $src = $match.Groups[2].Value
                $baseName = $src -replace '\.(png|jpg|jpeg|webp)(\?.*)?$', ''
                $mobileSrc = $baseName + '-mobile.webp'
                if ($src -match '\?') { $mobileSrc += $src.Substring($src.IndexOf('?')) }
                '<picture><source media="(max-width: 768px)" srcset="' + $mobileSrc + '"><img' + $match.Groups[1].Value + ' src="' + $src + '"' + $match.Groups[3].Value + '></picture>'
            })
        }
    }

    # Step 5: Lazy script before </body>
    if ($html -notmatch 'lazySections|ls=document\.querySelectorAll') {
        $html = $html -replace '\s*</body>', "$lazyScript`n</body>"
    }

    # Step 3: Defer language-switcher on mobile
    $html = $html -replace '<script\s+src="([^"]*language-switcher\.js[^"]*)"\s+defer\s*></script>', '<script>if(window.innerWidth>768){var s=document.createElement("script");s.src="$1";s.defer=true;document.body.appendChild(s);}</script>'
    $html = $html -replace "<script\s+src='([^']*language-switcher\.js[^']*)'\s+defer\s*></script>", '<script>if(window.innerWidth>768){var s=document.createElement("script");s.src="$1";s.defer=true;document.body.appendChild(s);}</script>'

    if ($html -ne $orig) {
        Set-Content -Path $file -Value $html -NoNewline
        $script:count++
    }
}

Write-Host "Updated $count HTML files"
