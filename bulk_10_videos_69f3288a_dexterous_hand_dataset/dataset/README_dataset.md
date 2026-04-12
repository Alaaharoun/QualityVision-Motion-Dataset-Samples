# Motion dataset export

## Overview

- **Job**: `bulk_10_videos_69f3288a`
- **Source**: **10 videos from Pexels (inferred from filenames)**
- **Action label**: `Dexterous Hand movements`
- **HQ exported frames**: **9228** (includes augmentation duplicates)

## Key metrics (quick table)

| Metric | Value |
|---|---:|
| Videos processed | 10 |
| Frames exported (HQ, incl. augmentations) | 9228 |
| Frames sampled (pre-augmentation candidates) | 4107 |
| Frames accepted (pre-augmentation) | 2307 |
| Accepted percentage (pre-aug / sampled) | 56.17% |
| Mean frame quality score (accepted) | 0.9645 |
| Mean avg landmark visibility (accepted) | 0.9290 |
| Mean lower-body visibility (accepted) | 0.0000 |
| Mean motion_local (accepted) | 1.0000 |
| Mean fps | 26.99 |
| Stride | 1 |

See `dataset/global_stats.json` and `dataset/export_quality_report.json` for full details.

## Buyer marketing (hand / dexterous exports)

- **Tagline:** Train your AI on real hand motion data — ready in minutes.
- **Commercial use:** Unlike many academic datasets, B2B exports are licensed for agreed commercial use — see **LICENSE_EXPORT.txt** in the ZIP and manifest license fields; structured copy also appears in **features.json** → `aggregate.buyer_marketing` and **global_stats.json** → `buyer_marketing`.
- **PyTorch:** see **examples/README_PYTORCH.md**.
- **Actions table:** **metadata/actions.csv** (`frame_id`, `action`).

## Processing applied

- **Gaussian smoothing** (temporal): enabled (x/y/z only; visibility is not smoothed)
- **Body normalization**: enabled (hip-centered + torso-scale) (`keypoints_body_normalized`, `body_normalization`)

## Layout

- `data.jsonl` — all accepted frames from all videos (global `frame_id`).
- `per_video/video_NNN.jsonl` — same schema, only frames from source index NNN.
- `per_video/rejected_NNN.jsonl` — low-quality / no-pose frames for that source.
- `low_quality_frames.jsonl` — all rejected rows across sources.
- `bulk_combined_manifest.json` — index of combined vs per-video files.
- `quality_distribution_histogram.json` — histogram of accepted pre-augmentation quality scores.
- `sample_frames_visualized/` — small PNG previews with keypoints overlaid.
- `use_cases.md` — practical use-case examples.
- `examples/preview_rows.jsonl` — medium sample for generating a ~40s skeleton-only preview.
- `viewer.html` — single-file local keypoint viewer (no server).
- `data.csv` — optional CSV export (enable with `MDE_EXPORT_CSV=1`).
- `coco_keypoints.json` — optional COCO-like keypoints-only JSON (enable with `MDE_EXPORT_COCO=1`).
- `features.json` — per-video sequence metrics (motion consistency, velocity proxies, etc.).
- `manifest.json` — job metadata and post-processing flags.
- `metadata/actions.csv` — `frame_id,action` (job-level label per row unless `hq.per_frame_actions`).
- `metadata/hand_activity.csv` — dexterous exports only: per-frame `hand_activity_class`, `grip_type_proxy`, `motion_class_rule`.
- `metadata/dataset_meta.json` — optional `camera_pov`, schema notes.

## Accepted percentage

- `accepted_percentage` is computed as **accepted (pre-augmentation) / sampled frames**.
- Exported frame count can exceed sampled frames when augmentations duplicate accepted rows.

## Dexterous Hand Movements (this export)

`manifest.json` sets **`dexterous_hand_export`: true**. Each accepted row in `data.jsonl` includes a **`dexterous_hand`** object and top-level **`motion_intelligence`** (version 3, hand domain) for buyer-ready hand analytics. Fields:

- **`finger_angles_deg`** — 2D flexion/spread proxies per finger chain (see `SCHEMA.md` for keys)
- **`grip_type_proxy`** — `pinch` | `precision` | `power` | `open` | `neutral` | `unknown`
- **`finger_tip_velocity_norm_per_sec`** — per-tip speeds (`*_tip_speed`) in normalized coords/sec
- **`finger_tip_speed_mean`** — mean tip speed for the frame
- **`hand_visibility_mean`** — mean landmark visibility
- **`dexterous_quality_proxy`** — hand-only quality score (0–1)
- **`motion_intelligence`** (inside `dexterous_hand`) — wrist speed, finger energy, grip change flag, `hand_activity_class` (`static` / `finger_active` / `hand_translating` / `manipulation`)

Aggregate hand motion stats: **`global_stats.json` → `motion_intelligence`** (`hand_activity_histogram`, `grip_type_histogram`). Regular pose-only exports omit this block.
