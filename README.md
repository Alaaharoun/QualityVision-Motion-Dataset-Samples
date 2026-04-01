# QualityVision Motion Dataset Samples

**High-quality 2D pose estimation data for walking** — HQ-filtered frames, temporal smoothing on accepted frames in the parent pipeline, and sequence-level diagnostics compatible with the [Quality Vision](https://github.com/Alaaharoun) Motion Dataset Engine export format.

This repository hosts **public pose-export samples** for **evaluation, demos, and pilot integrations**. It is **not** a full commercial release; larger batches and redistribution terms are negotiated separately.

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
| [`bulk_24_videos_6a173caf_dataset/`](./bulk_24_videos_6a173caf_dataset/) | **Primary sample:** full `dataset/` tree (JSONL, manifests, stats, per-video splits). |
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
2. **Full sample:** parse `bulk_24_videos_6a173caf_dataset/dataset/data.jsonl` — one JSON object per line (see [`bulk_24_videos_6a173caf_dataset/README.md`](./bulk_24_videos_6a173caf_dataset/README.md) for authentic vs augmented counts).
3. **Quick test:** parse `walking_sample_v1/data.jsonl` (small file).
4. Read `features.json` / `global_stats.json` under the folder you chose for aggregates.
5. (Optional) Regenerate preview images:

```bash
python scripts/render_pose_preview.py
```

Requirements: Python 3.10+ and `matplotlib` (`pip install matplotlib`).

## Format

- **Per frame:** `keypoints` dictionary (BlazePose-style landmark names), `timestamp_ms`, `action_label`, `frame_id`, etc.
- **Coordinates:** Normalized image space (see `features.json` notes).
- **License:** See [`LICENSE`](./LICENSE) (**CC BY-NC 4.0**). Commercial use **outside** the NC terms requires a **separate written agreement**.

## Roadmap

- Additional actions (e.g. running, turning) as separate sample folders.
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
