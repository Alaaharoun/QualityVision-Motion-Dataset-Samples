# QualityVision Motion Dataset Samples

**High-quality motion-export samples** — including **walking / locomotion** (full-body pose) and **Dexterous Hand movements** (21-point MediaPipe Hands + dexterous analytics). Exports use HQ filtering, temporal smoothing where enabled, and the same JSONL + metadata layout as the [Quality Vision](https://github.com/Alaaharoun) Motion Dataset Engine.

This repository hosts **public pose-export samples** for **evaluation, demos, and pilot integrations**. It is **not** a full commercial release; larger batches and redistribution terms are negotiated separately.

## Dexterous Hand movements — recommended free sample (2026, `bulk_9`)

**Best current public hand sample for robotics / manipulation pilots** (e.g. AgiBot, Unitree, UBTECH): **9** source clips, **wrist-relative** post-processing (`wrist_position`, `wrist_relative_keypoints`), dexterous **motion_intelligence** + grip / activity histograms, and **use_cases.md** scoped to dexterous work (not walking).

[`bulk_9_videos_933d5ad5_dataset/`](./bulk_9_videos_933d5ad5_dataset/) — production-style `dataset/` tree: merged `data.jsonl`, `per_video/`, `metadata/`, `global_stats.json`, `features.json`, `SCHEMA.md`, `ONEPAGER.md`.

| Metric | Value (see [`dataset/ONEPAGER.md`](./bulk_9_videos_933d5ad5_dataset/dataset/ONEPAGER.md)) |
|--------|----------------------------------------------------------------------------------------------------------------------------------|
| Job ID | `bulk_9_videos_933d5ad5` |
| Action label | **Dexterous Hand movements** |
| Videos processed | **9** |
| Exported rows in merged `data.jsonl` (HQ, incl. augmentations) | **9112** |
| Accepted frames (pre-augmentation) | **2278** |
| Acceptance rate (pre-aug / sampled) | **57.5%** |
| Mean quality score (accepted) | **~0.9715** |
| Mean landmark visibility (accepted) | **~0.943** |
| Keypoints | **MediaPipe Hands** (21 landmarks) |
| Post-processing | Gaussian smoothing + **wrist-relative** fields; hip-based body normalization is **not applied** to hand-only rows (see manifest notes) |
| Dexterous extras | Finger angles, grip heuristics, hand `motion_intelligence` (v3), activity / grip histograms |

**Full commercial / enterprise packs:** For **larger batches**, **custom scope**, or **licensing**, contact **info@qvision.space** and see [Dataset pricing](https://qvision.space/dataset-pricing). This repo stays a **free evaluation sample** only.

## Dexterous Hand movements — additional 10-video public sample (2026)

[`bulk_10_videos_69f3288a_dexterous_hand_dataset/`](./bulk_10_videos_69f3288a_dexterous_hand_dataset/) — alternate **10**-clip hand bulk export (see [`dataset/ONEPAGER.md`](./bulk_10_videos_69f3288a_dexterous_hand_dataset/dataset/ONEPAGER.md)): **9228** merged HQ rows (incl. augmentations), **2307** accepted pre-aug, mean quality **~0.9645**.

**Larger commercial offering (not in this repo):** Quality Vision can deliver **~140,000+ HQ frames** and **multi-clip** packages segmented for **specific, precise dexterous motions** — negotiated scope, licensing, and delivery format. See **Ready-made datasets** below and [`dataset-pricing`](https://qvision.space/dataset-pricing).

## Ready-made datasets (commercial)

Quality Vision runs a **public storefront** for **ready-made pose / motion dataset bundles** (JSONL exports + metadata, same engine layout as these samples). That is separate from the **free** samples in this repo:

- **Pricing & curated bundles:** [qvision.space/dataset-pricing](https://qvision.space/dataset-pricing)
- **Product site:** [qvision.space](https://qvision.space)

For licensing or custom scope, use the contact options on the site (e.g. **info@qvision.space**).

## Flagship: 24-video walking export (2026)

[`bulk_24_videos_6a173caf_dataset/`](./bulk_24_videos_6a173caf_dataset/) — full **Quality Vision Motion Dataset Engine** bulk package (same layout as production exports):

| Metric | Value |
|--------|--------|
| HQ-accepted frames (pre-augmentation) | **967** |
| Rows in merged `data.jsonl` | **2901** (includes augmentations: flip + keypoint noise, plus pipeline settings below) |
| Mean quality score (accepted frames) | **~0.82** |
| Sources | **24** walking clips; **no per-video frame cap** (`max_per_video_effective: 0` in `dataset/runtime_config.json`) |

Start from [`bulk_24_videos_6a173caf_dataset/dataset/data.jsonl`](./bulk_24_videos_6a173caf_dataset/dataset/data.jsonl) and [`run_diagnostics.json`](./bulk_24_videos_6a173caf_dataset/dataset/run_diagnostics.json) for per-source breakdown. Raw source videos are **not** stored in git (pose JSONL only).

## What’s inside

| Path | Contents |
|------|-----------|
| [`bulk_9_videos_933d5ad5_dataset/`](./bulk_9_videos_933d5ad5_dataset/) | **Dexterous Hand movements (recommended free sample):** 9-video hand bulk export with wrist-relative fields + ONEPAGER. |
| [`bulk_10_videos_69f3288a_dexterous_hand_dataset/`](./bulk_10_videos_69f3288a_dexterous_hand_dataset/) | **Dexterous Hand movements:** additional 10-video hand bulk export (JSONL + `metadata/` + ONEPAGER). |
| [`bulk_24_videos_6a173caf_dataset/`](./bulk_24_videos_6a173caf_dataset/) | **Primary walking sample:** full `dataset/` tree (JSONL, manifests, stats, per-video splits). |
| [`walking_sample_v1/`](./walking_sample_v1/) | **Compact legacy clip** (~80 frames) for quick parsing tests; older quality headline (~0.63 sequence score). |
| [`bulk_2_videos_28fb9459_dataset/`](./bulk_2_videos_28fb9459_dataset/) | **Compact running bulk export:** full `dataset/` tree for 2 running clips (includes per-video splits + rejected frames). |
| [`With Original videos/`](./With%20Original%20videos/) | Older pilot bulk folder (smaller export); kept for history. Prefer the **bulk_24** tree above for current numbers. |
| [`images/`](./images/) | Pose preview renders (regenerate with `scripts/render_pose_preview.py`). |
| [`docs/EULA.md`](./docs/EULA.md) | End-user terms for this sample distribution. |

### `walking_sample_v1` at a glance (legacy compact)

- **80 frames** of **walking**, image-normalized 2D landmarks (+ optional Layer 1.1 metadata where present).
- Derived from a **longer HQ-filtered export**; frames were **renumbered** for a compact GitHub-friendly subset.
- **Sequence quality score**: **0.6328** (see `global_stats.json` / `features.json`)
  - Mean landmark visibility: **0.7707**
  - Motion consistency: **0.4949** (method: `blend_smoothed_cv_mad_v1`)

### `bulk_2_videos_28fb9459_dataset` at a glance (compact running bulk)

[`bulk_2_videos_28fb9459_dataset/`](./bulk_2_videos_28fb9459_dataset/) is a small but **production-layout** bulk export for **running**.

| Metric | Value |
|--------|--------|
| Videos processed | **2** running clips |
| HQ-accepted frames (pre-augmentation) | **116** |
| Rows in merged `data.jsonl` | **348** (includes augmentations: horizontal flip + keypoint noise) |
| Accepted percentage | **56.86%** (pre-augmentation acceptance rate over sampled frames) |
| Mean quality score (accepted frames) | **0.8424** |
| Mean landmark visibility (accepted frames) | **0.8038** |
| Post-processing | Gaussian smoothing (**window=5**) + body normalization (`hip_center_torso_scale`) |
| Default stride | **6** |

It includes a full `dataset/` tree: merged `data.jsonl`, `low_quality_frames.jsonl`, per-video splits under `dataset/per_video/`, plus `manifest.json`, `runtime_config.json`, `global_stats.json`, and `export_quality_report.json`.

## Quick start

1. Clone the repository.
2. **Dexterous Hand movements (recommended):** read [`bulk_9_videos_933d5ad5_dataset/dataset/ONEPAGER.md`](./bulk_9_videos_933d5ad5_dataset/dataset/ONEPAGER.md), then parse [`bulk_9_videos_933d5ad5_dataset/dataset/data.jsonl`](./bulk_9_videos_933d5ad5_dataset/dataset/data.jsonl) (one JSON object per line). Alternate: [`bulk_10_videos_69f3288a_dexterous_hand_dataset/dataset/`](./bulk_10_videos_69f3288a_dexterous_hand_dataset/dataset/).
3. **Walking (flagship):** parse `bulk_24_videos_6a173caf_dataset/dataset/data.jsonl` — one JSON object per line (see [`bulk_24_videos_6a173caf_dataset/README.md`](./bulk_24_videos_6a173caf_dataset/README.md) for authentic vs augmented counts).
4. **Quick test:** parse `walking_sample_v1/data.jsonl` (small file).
5. Read `features.json` / `global_stats.json` under the folder you chose for aggregates.
6. (Optional) Regenerate preview images:

```bash
python scripts/render_pose_preview.py
```

Requirements: Python 3.10+ and `matplotlib` (`pip install matplotlib`).

## Format

- **Walking / full-body samples:** `keypoints` use **BlazePose-style** landmark names (33 landmarks), `timestamp_ms`, `action_label`, `frame_id`, etc.
- **Dexterous Hand movements samples:** `keypoints` use **MediaPipe Hands** landmark names (21 points); rows may include **`dexterous_hand`** and hand-centric **`motion_intelligence`** — see `SCHEMA.md` / `ONEPAGER.md` inside that folder.
- **Coordinates:** Normalized image space (see `features.json` notes).
- **License:** See [`LICENSE`](./LICENSE) (**CC BY-NC 4.0**). Commercial use **outside** the NC terms requires a **separate written agreement**.

## Roadmap

- Additional actions (e.g. running, turning) as separate sample folders.
- Optional: Hugging Face mirror for the **Dexterous Hand movements** bulk tree (same pattern as walking upload scripts).
- Optional Hugging Face mirrors for the **bulk** export (see `scripts/upload_bulk_to_huggingface.ps1`).

## Citation

If you use this sample in research or demos, please cite the repository URL:

```text
https://github.com/Alaaharoun/QualityVision-Motion-Dataset-Samples
```

## Hugging Face Datasets

| Hub repo | Contents | Upload script |
|----------|----------|----------------|
| [Alaaharoun/QualityVision-walking-sample](https://huggingface.co/datasets/Alaaharoun/QualityVision-walking-sample) | Compact **`walking_sample_v1`** (+ dataset card `README_HF_DATASET.md`) | `scripts/upload_to_huggingface.ps1` |
| Create e.g. `Alaaharoun/QualityVision-bulk-24v-walking` (empty dataset repo on HF) | Full **`bulk_24_videos_6a173caf_dataset/dataset/`** tree | `scripts/upload_bulk_to_huggingface.ps1` |

Prerequisites: `pip install -U huggingface_hub` and `hf auth login` (or set `HF_TOKEN`).

```powershell
# Compact sample (legacy card: README_HF_DATASET.md)
powershell -ExecutionPolicy Bypass -File scripts/upload_to_huggingface.ps1

# Full bulk JSONL package (edit $RepoId inside script to match your new HF dataset)
powershell -ExecutionPolicy Bypass -File scripts/upload_bulk_to_huggingface.ps1
```

The bulk upload uses `README_HF_BULK.md` as the Hub dataset card `README.md`.

## Publish to GitHub (empty remote)

From this folder:

```bash
git init
git add .
git commit -m "Initial public walking sample (80 frames) + docs + preview image"
git branch -M main
git remote add origin https://github.com/Alaaharoun/QualityVision-Motion-Dataset-Samples.git
git push -u origin main
```

**Suggested GitHub metadata**

- **Description:** `High-quality 2D pose estimation dataset for walking (HQ filtered + temporal smoothing). Free pilot samples.`
- **Topics:** `pose-estimation`, `dataset`, `walking`, `motion-capture`, `mediapipe`, `machine-learning`, `robotics`
- **Website:** [https://qvision.space](https://qvision.space) (ready-made datasets: [dataset-pricing](https://qvision.space/dataset-pricing))

## Contact

Open an issue for pilot feedback, integration questions, or licensing for full datasets. For **purchasing ready-made exports**, see [Dataset pricing](https://qvision.space/dataset-pricing) on the Quality Vision site.
