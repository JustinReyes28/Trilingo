param([switch]$SkipOpen)
$ErrorActionPreference = 'Stop'
$projectRoot = Split-Path -Parent $PSScriptRoot
$python = Join-Path $projectRoot '.venv\Scripts\python.exe'
$frontend = Join-Path $projectRoot 'frontend'
if (-not (Test-Path -LiteralPath $python)) { throw 'Create .venv and install backend/requirements.lock using README first.' }
$node = (Get-Command node -ErrorAction Stop).Source
if (-not (Test-Path -LiteralPath (Join-Path $frontend 'node_modules/vite/bin/vite.js'))) { throw 'Install frontend dependencies using README first.' }
$backendProcess = $null
$frontendProcess = $null
try {
    Push-Location (Join-Path $projectRoot 'backend')
    try {
        & $python -m alembic upgrade head
        if ($LASTEXITCODE -ne 0) { throw 'Migration failed. No service was started.' }
        & $python -m app.cli import
        if ($LASTEXITCODE -ne 0) { throw 'Content import failed. No service was started.' }
        $configJson = & $python -m app.start_config
        $config = $configJson | ConvertFrom-Json
    } finally { Pop-Location }
    $apiOrigin = 'http://' + $config.host + ':' + $config.port
    $listener = Get-NetTCPConnection -LocalPort $config.port -State Listen -ErrorAction SilentlyContinue
    if ($listener) { throw ('Backend port ' + $config.port + ' is already in use. Stop that service or choose another port.') }
    if (Get-NetTCPConnection -LocalPort 5173 -State Listen -ErrorAction SilentlyContinue) { throw 'Frontend port 5173 is already in use.' }
    $logDir = Join-Path $projectRoot '.data'
    New-Item -ItemType Directory -Force -Path $logDir | Out-Null
    $backendProcess = Start-Process -FilePath $python -ArgumentList @('-m','app') -WorkingDirectory (Join-Path $projectRoot 'backend') -WindowStyle Hidden -PassThru -RedirectStandardOutput (Join-Path $logDir 'backend.log') -RedirectStandardError (Join-Path $logDir 'backend-errors.log')
    $env:VITE_API_BASE_URL = $apiOrigin + '/api/v1'
    $frontendProcess = Start-Process -FilePath $node -ArgumentList @('node_modules/vite/bin/vite.js','--host','127.0.0.1','--port','5173') -WorkingDirectory $frontend -WindowStyle Hidden -PassThru -RedirectStandardOutput (Join-Path $logDir 'frontend.log') -RedirectStandardError (Join-Path $logDir 'frontend-errors.log')
    $ready = $false
    for ($attempt=0; $attempt -lt 30; $attempt++) {
        if ($backendProcess.HasExited -or $frontendProcess.HasExited) { throw 'A service exited during startup. Check .data logs.' }
        try {
            $health = Invoke-RestMethod -Uri ($apiOrigin + '/api/v1/health') -TimeoutSec 1
            $page = Invoke-WebRequest -Uri 'http://127.0.0.1:5173' -UseBasicParsing -TimeoutSec 1
            if ($health.status -eq 'ok' -and $page.StatusCode -eq 200) { $ready=$true; break }
        } catch [System.Net.WebException] { }
        Start-Sleep -Milliseconds 300
    }
    if (-not $ready) { throw 'Startup timed out. Check .data logs and README troubleshooting.' }
    Write-Host 'Trilingo is ready at http://127.0.0.1:5173. Press Ctrl+C here to stop both services.'
    if (-not $SkipOpen) { Start-Process 'http://127.0.0.1:5173' }
    while (-not $backendProcess.HasExited -and -not $frontendProcess.HasExited) { Start-Sleep -Seconds 1 }
} finally {
    foreach ($owned in @($frontendProcess,$backendProcess)) {
        if ($null -ne $owned -and -not $owned.HasExited) { Stop-Process -Id $owned.Id }
    }
}
