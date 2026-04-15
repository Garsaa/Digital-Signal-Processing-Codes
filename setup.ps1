$ErrorActionPreference = "Stop"

$projectRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$pythonCmd = Get-Command python -ErrorAction SilentlyContinue

if (-not $pythonCmd) {
    Write-Error "Python nao encontrado no PATH. Instale o Python 3.11+ e tente novamente."
}

$venvPython = Join-Path $projectRoot ".venv\\Scripts\\python.exe"
$requirementsFile = Join-Path $projectRoot "requirements-notebook.txt"

if (-not (Test-Path $venvPython)) {
    Write-Host "Criando ambiente virtual em .venv..." -ForegroundColor Cyan
    & python -m venv (Join-Path $projectRoot ".venv")
}

Write-Host "Atualizando pip..." -ForegroundColor Cyan
& $venvPython -m pip install --upgrade pip

Write-Host "Instalando dependencias do projeto..." -ForegroundColor Cyan
& $venvPython -m pip install -r $requirementsFile

Write-Host ""
Write-Host "Ambiente pronto." -ForegroundColor Green
Write-Host "No VS Code, selecione o interpretador .venv\\Scripts\\python.exe"

