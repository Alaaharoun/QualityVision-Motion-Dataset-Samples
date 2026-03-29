# Upload walking_sample_v1 + Dataset README to Hugging Face Datasets
# Repo: https://huggingface.co/datasets/Alaaharoun/QualityVision-walking-sample
#
# Prerequisites:
#   pip install -U huggingface_hub
#   hf auth login
#   OR:  $env:HF_TOKEN = "hf_..."   (write token from https://huggingface.co/settings/tokens )
#
# Usage (from repo root):
#   powershell -ExecutionPolicy Bypass -File scripts/upload_to_huggingface.ps1

$ErrorActionPreference = "Stop"
$RepoRoot = Split-Path -Parent $PSScriptRoot
$RepoId = "Alaaharoun/QualityVision-walking-sample"
$SampleDir = Join-Path $RepoRoot "walking_sample_v1"
$Staging = Join-Path $env:TEMP "qv_hf_staging_$(Get-Random)"

if (-not (Test-Path $SampleDir)) {
    Write-Error "Missing folder: $SampleDir"
}

New-Item -ItemType Directory -Path $Staging -Force | Out-Null
Copy-Item -Path (Join-Path $RepoRoot "README_HF_DATASET.md") -Destination (Join-Path $Staging "README.md") -Force
# Frame rows at repo root; other JSON reports under metadata/ so HF viewer does not merge schemas.
Copy-Item -Path (Join-Path $SampleDir "data.jsonl") -Destination (Join-Path $Staging "data.jsonl") -Force
$meta = Join-Path $Staging "metadata"
New-Item -ItemType Directory -Path $meta -Force | Out-Null
foreach ($name in @("features.json", "global_stats.json", "manifest.json", "export_quality_report.json", "README_sample.md")) {
    $src = Join-Path $SampleDir $name
    if (Test-Path $src) {
        Copy-Item -Path $src -Destination (Join-Path $meta $name) -Force
    }
}

Write-Host "Staging: $Staging"
Write-Host "Uploading to $RepoId ..."
Write-Host "If this fails with 401, run: hf auth login"
Write-Host "Or set: `$env:HF_TOKEN = 'hf_...' (from https://huggingface.co/settings/tokens )"

$args = @(
    "upload", $RepoId, $Staging, ".",
    "--repo-type=dataset",
    "--commit-message=Walking sample: data.jsonl at root; metadata/*.json for viewer-safe layout + README configs"
)
if ($env:HF_TOKEN) {
    $args += "--token", $env:HF_TOKEN
}
& hf @args

Remove-Item -Recurse -Force $Staging -ErrorAction SilentlyContinue
Write-Host "Done."
