param(
  [string]$repoName = "loan-approval-service"
)
function Test-Command($name) {
  $null -ne (Get-Command $name -ErrorAction SilentlyContinue)
}
Write-Host "Working directory: $(Get-Location)"
Write-Host "`nStep 0: Verify mvn compile will succeed`n"
if (Test-Path ".\mvnw.cmd") {
  Write-Host "Running: .\mvnw.cmd clean compile -f pom.xml"
  $env:JAVA_HOME='C:\Program Files\Eclipse Adoptium\jdk-17.0.19.10-hotspot'
  $env:Path="$env:JAVA_HOME\bin;$env:Path"
  .\mvnw.cmd clean compile -f pom.xml
  if ($LASTEXITCODE -ne 0) {
    Write-Warning "mvn compile failed"
    exit 1
  }
  Write-Host "OK - mvn compile succeeded"
}
Write-Host "`nStep 1: Check prerequisites`n"
if (-not (Command-Exists git)) {
  Write-Host "ERROR: git not found. Install from https://git-scm.com"
  exit 1
}
Write-Host "OK - git found: $(git --version)"
if (-not (Command-Exists gh)) {
  Write-Host "ERROR: gh not found. Install from https://cli.github.com"
  exit 1
}
Write-Host "OK - gh found"
Write-Host "`nStep 2: Ensure gh is authenticated`n"
gh auth status
if ($LASTEXITCODE -ne 0) {
  Write-Host "Running: gh auth login"
  gh auth login
  if ($LASTEXITCODE -ne 0) {
    Write-Host "ERROR: gh auth login failed"
    exit 1
  }
}
Write-Host "OK - authenticated"
Write-Host "`nStep 3: Initialize git repo`n"
if (-not (Test-Path .git)) {
  git init
  Write-Host "OK - git repo initialized"
} else {
  Write-Host "OK - git repo already exists"
}
Write-Host "`nStep 4: Configure git user`n"
$uname = git config user.name
if (-not $uname) {
  $name = Read-Host "Enter your full name"
  git config --global user.name $name
}
$uemail = git config user.email
if (-not $uemail) {
  $email = Read-Host "Enter your email"
  git config --global user.email $email
}
Write-Host "OK - git configured"
Write-Host "`nStep 5: Stage and commit`n"
git add -A
git commit -m "Initial import: fixed LoanApplication and LoanApplicationRepository"
Write-Host "OK - committed"
Write-Host "`nStep 6: Create GitHub repo and push`n"
$remoteExists = git remote get-url origin 2>$null
if ($remoteExists) {
  Write-Host "Remote origin already exists: $remoteExists"
  $resp = Read-Host "Overwrite with github.com/$repoName (y/N)?"
  if ($resp -ne 'y' -and $resp -ne 'Y') {
    exit 0
  }
  git remote remove origin
}
Write-Host "Creating repository on GitHub: $repoName"
gh repo create $repoName --public --source=. --remote=origin --push
if ($LASTEXITCODE -ne 0) {
  Write-Host "ERROR: gh repo create failed"
  exit 1
}
Write-Host "`nStep 7: Verify`n"
Write-Host "Git remote:"
git remote -v
Write-Host "`nGitHub auth status:"
gh auth status
Write-Host "`nRepository info:"
gh repo view $repoName --json name,url
Write-Host "`nDone! Repository created and code pushed to GitHub."
Write-Host "Open in browser: https://github.com/$(gh api user --jq '.login')/$repoName"
