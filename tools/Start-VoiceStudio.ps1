param(
    [switch]$RecreateEnvironment
)

$ErrorActionPreference = 'Stop'

$RepoRoot = Split-Path -Parent $PSScriptRoot
Set-Location $RepoRoot

$VenvRoot = Join-Path $RepoRoot '.venv-voice-gui'
$VenvPython = Join-Path $VenvRoot 'Scripts\python.exe'

function Test-PythonVersion {
    param([Parameter(Mandatory)][string]$Version)

    if (-not (Get-Command py -ErrorAction SilentlyContinue)) {
        return $false
    }

    & py "-$Version" -c "import sys; raise SystemExit(0 if sys.version_info < (3, 15) else 1)" 2>$null
    return ($LASTEXITCODE -eq 0)
}

function New-VoiceGuiEnvironment {
    $preferredVersions = @('3.14', '3.13', '3.12')
    $selected = $null

    foreach ($version in $preferredVersions) {
        if (Test-PythonVersion -Version $version) {
            $selected = $version
            break
        }
    }

    if (-not $selected) {
        throw @'
PySide6 currently requires Python < 3.15.
No compatible Python 3.14, 3.13, or 3.12 interpreter was found through the Windows py launcher.

Install Python 3.14 x64, then run this launcher again.
You can inspect installed interpreters with:
  py -0p
'@
    }

    Write-Host "Creating Voice Studio GUI environment with Python $selected..."
    & py "-$selected" -m venv $VenvRoot
    if ($LASTEXITCODE -ne 0) {
        throw "Failed to create $VenvRoot with Python $selected."
    }

    & $VenvPython -m pip install --upgrade pip
    if ($LASTEXITCODE -ne 0) {
        throw 'Failed to upgrade pip in the GUI environment.'
    }

    & $VenvPython -m pip install -r requirements-voice-gui.txt
    if ($LASTEXITCODE -ne 0) {
        throw 'Failed to install Voice Studio GUI dependencies.'
    }
}

if ($RecreateEnvironment -and (Test-Path $VenvRoot)) {
    Write-Host "Removing existing GUI environment: $VenvRoot"
    Remove-Item $VenvRoot -Recurse -Force
}

if (-not (Test-Path $VenvPython)) {
    New-VoiceGuiEnvironment
}
else {
    & $VenvPython -c "import PySide6, google.genai" 2>$null
    if ($LASTEXITCODE -ne 0) {
        Write-Host 'GUI environment exists but dependencies are incomplete. Repairing...'
        & $VenvPython -m pip install -r requirements-voice-gui.txt
        if ($LASTEXITCODE -ne 0) {
            throw 'Failed to repair Voice Studio GUI dependencies.'
        }
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

& $VenvPython .\tools\voice_studio_gui.py

if ($LASTEXITCODE -ne 0) {
    throw "Voice Studio exited with code $LASTEXITCODE."
}
