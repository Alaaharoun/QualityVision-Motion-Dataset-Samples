# Upload bulk_24_videos_6a173caf_dataset/dataset/* + README_HF_BULK.md to Hugging Face Datasets
#
# Create an empty dataset repo on HF first (e.g. QualityVision-bulk-24v-walking), then set $RepoId below.
#
# Prerequisites:
#   pip install -U huggingface_hub
#   hf auth login
#   OR:  $env:HF_TOKEN = "hf_..."
#
# Usage (from repo root):
#   powershell -ExecutionPolicy Bypass -File scripts/upload_bulk_to_huggingface.ps1

$ErrorActionPreference = "Stop"
$RepoRoot = Split-Path -Parent $PSScriptRoot
# Create this dataset at https://huggingface.co/new-dataset if it does not exist
$RepoId = "Alaaharoun/QualityVision-bulk-24v-walking"
$DatasetDir = Join-Path $RepoRoot "bulk_24_videos_6a173caf_dataset\dataset"
$Staging = Join-Path $env:TEMP "qv_hf_bulk_staging_$(Get-Random)"

if (-not (Test-Path $DatasetDir)) {
    Write-Error "Missing folder: $DatasetDir"
}

New-Item -ItemType Directory -Path $Staging -Force | Out-Null
Copy-Item -Path (Join-Path $RepoRoot "README_HF_BULK.md") -Destination (Join-Path $Staging "README.md") -Force
Copy-Item -Path "$DatasetDir\*" -Destination $Staging -Recurse -Force

Write-Host "Staging: $Staging"
Write-Host "Uploading to $RepoId ..."
Write-Host "If this fails with 401, run: hf auth login"
Write-Host "Or set: `$env:HF_TOKEN = 'hf_...'"

$hfArgs = @(
    "upload", $RepoId, $Staging, ".",
    "--repo-type=dataset",
    "--commit-message=Bulk 24-video walking export: 967 HQ frames, 2901 merged rows, quality mean ~0.82"
)
if ($env:HF_TOKEN) {
    $hfArgs += "--token", $env:HF_TOKEN
}
& hf @hfArgs

Remove-Item -Recurse -Force $Staging -ErrorAction SilentlyContinue
Write-Host "Done."
