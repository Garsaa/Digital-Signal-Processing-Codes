param(
    [Parameter(Mandatory = $true, ValueFromRemainingArguments = $true)]
    [string[]]$Packages
)

$ErrorActionPreference = "Stop"

$projectRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$venvPython = Join-Path $projectRoot ".venv\\Scripts\\python.exe"
$requirementsFile = Join-Path $projectRoot "requirements-notebook.txt"

if (-not (Test-Path $venvPython)) {
    Write-Error "Ambiente .venv nao encontrado. Rode .\\setup.ps1 antes."
}

Write-Host "Instalando: $($Packages -join ', ')" -ForegroundColor Cyan
& $venvPython -m pip install @Packages

$existing = @()
if (Test-Path $requirementsFile) {
    $existing = Get-Content $requirementsFile | Where-Object { $_.Trim() -ne "" }
}

$updated = [System.Collections.Generic.List[string]]::new()
foreach ($line in $existing) {
    $updated.Add($line)
}

foreach ($package in $Packages) {
    if ($updated -notcontains $package) {
        $updated.Add($package)
    }
}

$updated |
    Sort-Object -Unique |
    Set-Content -Path $requirementsFile

Write-Host "requirements-notebook.txt atualizado." -ForegroundColor Green
