# Migrate blog posts to topic/articles/slug/ structure with pretty URLs (Option C)
# Run from project root: .\scripts\migrate-blog-urls.ps1

$ErrorActionPreference = "Stop"
$baseDir = Split-Path -Parent $PSScriptRoot
if (-not (Test-Path "$baseDir\blog")) { throw "Run from project root or ensure blog folder exists" }
Set-Location $baseDir

$topicMap = @{
    "sba-loans" = @(
        "what-do-lenders-look-for-sba-loan-approval", "can-you-use-sba-loan-to-buy-a-business",
        "sba-loan-vs-business-line-of-credit", "sba-7a-vs-504-loan", "what-credit-score-needed-sba-loan",
        "how-long-sba-loan-approval", "how-much-down-payment-required-sba-loan", "sba-loan-basics"
    )
    "equipment-financing" = @(
        "what-credit-score-needed-equipment-financing", "do-you-need-down-payment-for-equipment-financing",
        "what-benefits-does-lease-have-equipment-financing", "equipment-leasing-vs-loan-which-is-better",
        "can-you-finance-used-equipment", "how-fast-can-equipment-financing-be-approved",
        "what-are-typical-equipment-financing-rates", "what-do-lenders-look-at-equipment-financing-approval",
        "can-equipment-financing-help-build-business-credit", "how-equipment-financing-works"
    )
    "business-line-of-credit" = @(
        "what-are-typical-business-line-of-credit-rates", "business-line-of-credit-vs-term-loan",
        "what-credit-score-needed-business-line-of-credit", "do-you-need-collateral-business-line-of-credit",
        "how-fast-can-you-get-approved-business-line-of-credit", "what-do-lenders-look-for-business-line-of-credit",
        "secured-vs-unsecured-business-line-of-credit"
    )
    "working-capital-loans" = @(
        "what-is-working-capital-loan-how-does-it-work", "working-capital-loan-vs-business-line-of-credit",
        "what-credit-score-needed-working-capital-loan", "how-fast-can-you-get-working-capital-loan",
        "what-do-lenders-look-for-working-capital-loan-application", "how-much-can-you-qualify-for-working-capital-loan",
        "when-is-working-capital-loan-not-right-option"
    )
    "business-term-loans" = @(
        "how-much-can-you-qualify-for-business-term-loan", "secured-vs-unsecured-business-term-loan",
        "when-is-business-term-loan-not-right-option", "how-fast-can-you-get-business-term-loan",
        "what-credit-score-needed-business-term-loan", "business-term-loan-vs-line-of-credit",
        "what-do-lenders-look-for-business-term-loan"
    )
    "commercial-real-estate-loans" = @(
        "cash-out-refinance-commercial-property", "owner-occupied-vs-investment-commercial-property-loan",
        "sba-504-vs-conventional-commercial-real-estate-loan", "how-long-close-commercial-real-estate-loan",
        "what-credit-score-needed-commercial-real-estate-loan", "how-much-down-payment-required-commercial-property-loan",
        "what-do-lenders-look-for-commercial-real-estate-loan"
    )
    "commercial-bridge-loans" = @(
        "commercial-bridge-loan-vs-hard-money-loan", "commercial-bridge-loan-vs-sba-loan",
        "when-should-you-use-commercial-bridge-loan", "how-fast-can-you-close-commercial-bridge-loan",
        "what-do-lenders-look-for-commercial-bridge-loan"
    )
    "fix-and-flip" = @(
        "what-do-lenders-look-for-fix-and-flip-loan", "what-is-arv-fix-and-flip-loan",
        "fix-and-flip-vs-hard-money-loan", "what-is-maximum-ltv-fix-and-flip-loan",
        "how-fast-can-you-close-fix-and-flip-loan", "what-credit-score-needed-fix-and-flip-loan",
        "how-much-down-payment-fix-and-flip-loan", "typical-fix-and-flip-loan-rates"
    )
    "revenue-based-financing" = @(
        "how-fast-can-you-get-revenue-based-financing", "how-much-can-you-qualify-for-revenue-based-financing",
        "what-do-lenders-look-for-revenue-based-financing", "what-is-revenue-based-financing-how-does-it-work",
        "revenue-based-financing-vs-merchant-cash-advance", "what-credit-score-needed-revenue-based-financing"
    )
    "securities-based-lending" = @(
        "when-should-you-use-securities-based-lending", "how-does-securities-based-lending-work",
        "what-are-the-risks-of-securities-based-lending", "how-much-can-you-borrow-with-securities-based-lending"
    )
}

# Build slug->topic reverse map
$slugToTopic = @{}
foreach ($topic in $topicMap.Keys) {
    foreach ($slug in $topicMap[$topic]) {
        $slugToTopic[$slug] = $topic
    }
}

function Transform-ArticlePaths {
    param([string]$content, [string]$topic, [string]$slug)
    $root = "../../../"
    
    # 1. Canonical and og:url - new pretty URL
    $content = $content -replace "https://www\.axiantpartners\.com/blog/$([regex]::Escape($slug))\.html", "https://www.axiantpartners.com/$topic/articles/$slug/"
    
    # 2. Back link and hub link: ../something-blog.html -> ../../ (topic hub)
    $content = $content -replace 'href="\.\./[\w-]+-blog\.html"', 'href="../../"'
    
    # 3. Same-topic article links: ./other.html -> ../other-slug/ (BEFORE general ../ replace)
    foreach ($otherSlug in $topicMap[$topic]) {
        if ($otherSlug -ne $slug) {
            $content = $content -replace "href=`"\./$([regex]::Escape($otherSlug))\.html`"", "href=`"../$otherSlug/`""
        }
    }
    
    # 4. Cross-topic article links: ./other.html -> ../../other-topic/articles/other-slug/
    foreach ($s in $slugToTopic.Keys) {
        if ($slugToTopic[$s] -ne $topic) {
            $otherTopic = $slugToTopic[$s]
            $content = $content -replace "href=`"\./$([regex]::Escape($s))\.html`"", "href=`"../../$otherTopic/articles/$s/`""
        }
    }
    
    # 5. Root links: ../ anything else -> ../../../ (index, match, sba-loans.html, blog.html, etc.)
    $content = $content -replace 'href="\.\./([^"]+)"', 'href="../../../$1"'
    $content = $content -replace 'src="\.\./([^"]+)"', 'src="../../../$1"'
    
    return $content
}

Write-Host "Migrating blog posts..." -ForegroundColor Cyan
$migrated = 0
foreach ($topic in $topicMap.Keys) {
    foreach ($slug in $topicMap[$topic]) {
        $src = "blog\$slug.html"
        if (-not (Test-Path $src)) { 
            Write-Host "  Skip (not found): $src" -ForegroundColor Yellow
            continue 
        }
        $destDir = "$topic\articles\$slug"
        $destFile = "$destDir\index.html"
        if (Test-Path $destFile) {
            Write-Host "  Skip (exists): $destFile" -ForegroundColor Gray
            continue
        }
        New-Item -ItemType Directory -Path $destDir -Force | Out-Null
        $content = Get-Content $src -Raw
        $content = Transform-ArticlePaths $content $topic $slug
        Set-Content $destFile -Value $content -NoNewline
        Write-Host "  Migrated: $slug -> $destFile" -ForegroundColor Green
        $migrated++
    }
}
Write-Host "`nMigrated $migrated posts." -ForegroundColor Cyan
