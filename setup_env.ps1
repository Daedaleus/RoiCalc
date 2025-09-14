# Check if venv exists
if (!(Test-Path -Path "venv")) {
    Write-Host "Creating virtual environment..."
    python -m venv venv
}

# Activate venv
$venvActivate = ".\venv\Scripts\Activate.ps1"
Write-Host "Activating virtual environment..."
. $venvActivate

# Install requirements
Write-Host "Installing requirements..."
pip install -r requirements.txt
