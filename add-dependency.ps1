param(
    [Parameter(Mandatory = $true, ValueFromRemainingArguments = $true)]
    [string[]]$Packages
)

$ErrorActionPreference = "Stop"

$projectRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$managerScript = Join-Path $projectRoot "scripts\\manage_env.py"
$pythonCmd = Get-Command python -ErrorAction SilentlyContinue
$pyLauncher = Get-Command py -ErrorAction SilentlyContinue

if ($pythonCmd) {
    & $pythonCmd.Source $managerScript add @Packages
    exit $LASTEXITCODE
}
elseif ($pyLauncher) {
    & $pyLauncher.Source -3 $managerScript add @Packages
    exit $LASTEXITCODE
}
else {
    Write-Error "Python nao encontrado no PATH. Instale o Python 3.11+ e tente novamente."
}
