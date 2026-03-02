# Push to GitHub - Run this from the project folder in Cursor's terminal
# Usage: .\push-to-github.ps1

$ErrorActionPreference = "Stop"
Write-Host "=== Push to GitHub ===" -ForegroundColor Cyan
Write-Host "Current folder: $(Get-Location)" -ForegroundColor Yellow
Write-Host ""

# Check we're in a git repo
if (-not (Test-Path .git)) {
    Write-Host "ERROR: No .git folder found. Run this from the project root (axiant-partners-main)." -ForegroundColor Red
    exit 1
}

Write-Host "1. Git status (before add):" -ForegroundColor Cyan
git status

Write-Host ""
Write-Host "2. Staging all changes..." -ForegroundColor Cyan
git add -A

Write-Host ""
Write-Host "3. Git status (after add):" -ForegroundColor Cyan
git status

Write-Host ""
Write-Host "4. Committing..." -ForegroundColor Cyan
$commitMsg = "Update site - $(Get-Date -Format 'yyyy-MM-dd HH:mm')"
git commit -m $commitMsg
if ($LASTEXITCODE -ne 0) {
    Write-Host "No changes to commit (working tree clean). Pushing any existing commits..." -ForegroundColor Yellow
}

Write-Host ""
Write-Host "5. Pushing to GitHub..." -ForegroundColor Cyan
git push origin main
if ($LASTEXITCODE -eq 0) {
    Write-Host ""
    Write-Host "SUCCESS: Push completed." -ForegroundColor Green
} else {
    Write-Host ""
    Write-Host "PUSH FAILED. Check errors above. Common causes: auth, network, or branch conflict." -ForegroundColor Red
    exit 1
}
