param(
    [switch]$InstallDependencies
)

$ErrorActionPreference = 'Stop'

$RepoRoot = Split-Path -Parent $PSScriptRoot
Set-Location $RepoRoot

function Test-PythonModule {
    param([Parameter(Mandatory)][string]$Name)

    & python -c "import $Name" 2>$null
    return ($LASTEXITCODE -eq 0)
}

if (-not (Get-Command python -ErrorAction SilentlyContinue)) {
    throw 'Python was not found in PATH.'
}

if (-not (Test-PythonModule -Name 'PySide6')) {
    if (-not $InstallDependencies) {
        $answer = Read-Host 'PySide6 is missing. Install Voice Studio GUI dependencies now? [Y/n]'
        if ($answer -and $answer -notmatch '^(?i)y(es)?$|^(?i)j(a)?$') {
            throw 'PySide6 is required. Run this script again with -InstallDependencies.'
        }
    }

    & python -m pip install -r requirements-voice-gui.txt
    if ($LASTEXITCODE -ne 0) {
        throw "Dependency installation failed with exit code $LASTEXITCODE."
    }
}

if ([string]::IsNullOrWhiteSpace($env:GEMINI_API_KEY)) {
    Write-Host ''
    Write-Host 'GEMINI_API_KEY is not set in this PowerShell process.'
    $secureKey = Read-Host 'Paste Gemini API key' -AsSecureString
    $ptr = [Runtime.InteropServices.Marshal]::SecureStringToBSTR($secureKey)

    try {
        $env:GEMINI_API_KEY = [Runtime.InteropServices.Marshal]::PtrToStringBSTR($ptr).Trim()
    }
    finally {
        [Runtime.InteropServices.Marshal]::ZeroFreeBSTR($ptr)
    }

    if ([string]::IsNullOrWhiteSpace($env:GEMINI_API_KEY)) {
        throw 'No Gemini API key was supplied.'
    }
}

Remove-Item Env:GOOGLE_API_KEY -ErrorAction SilentlyContinue

& python .\tools\voice_pipeline.py gui

if ($LASTEXITCODE -ne 0) {
    throw "Voice Studio exited with code $LASTEXITCODE."
}
