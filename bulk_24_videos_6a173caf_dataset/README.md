# Bulk export: 24 videos (walking)

Engine job id: `bulk_24_videos_6a173caf`.

| | |
|---|---|
| **HQ-accepted frames (pre-augmentation)** | **967** (sum over sources in `dataset/run_diagnostics.json` → `per_video[].frames_accepted`) |
| **Rows in merged `dataset/data.jsonl`** | **2901** (includes Gaussian-smoothed export + horizontal flip + keypoint noise augmentations where enabled) |
| **Mean quality score (accepted frames)** | **~0.82** (`export_quality_report.json` / `global_stats.json`) |
| **Sources** | 24 clips; `max_per_video_effective: 0` in `runtime_config.json` (no per-video frame cap) |

## Contents

- **`dataset/`** — full Quality Vision Motion Dataset Engine tree: `data.jsonl`, `per_video/`, manifests, `run_diagnostics.json`, `runtime_config.json`, etc. This is what is tracked on GitHub.
- **`Videos/`** (if present locally) — optional copies of source `.mp4` files for your own review; **not** committed (see repo root `.gitignore`).

## License

Same as repository root: **CC BY-NC 4.0** unless otherwise agreed in writing for commercial use.
