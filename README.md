# QualityVision Motion Dataset Samples

**High-quality 2D pose estimation data for walking** — HQ-filtered frames, temporal smoothing on accepted frames in the parent pipeline, and sequence-level diagnostics compatible with the [Quality Vision](https://github.com/Alaaharoun) Motion Dataset Engine export format.

This repository hosts **small public samples** (typically **50–100 frames**) for **free evaluation, pilot integrations, and feedback**. It is **not** a full commercial release; larger batches and redistribution terms are negotiated separately.

## What’s inside

| Path | Contents |
|------|-----------|
| [`walking_sample_v1/`](./walking_sample_v1/) | Example walking clip: `data.jsonl`, `features.json`, `global_stats.json`, `manifest.json`, `export_quality_report.json`. |
| [`With Original videos/`](./With%20Original%20videos/) | Full bulk export package (larger `data.jsonl` + full `dataset/` tree), kept for transparency / pilot review. |
| [`images/`](./images/) | Pose preview renders (regenerate with `scripts/render_pose_preview.py`). |
| [`docs/EULA.md`](./docs/EULA.md) | End-user terms for this sample distribution. |

### `walking_sample_v1` at a glance

- **80 frames** of **walking**, image-normalized 2D landmarks (+ optional Layer 1.1 metadata where present).
- Derived from a **longer HQ-filtered export**; frames were **renumbered** for a compact GitHub-friendly subset.
- **Sequence quality score** ≈ **0.63** (see `global_stats.json` / `features.json`); **`motion_consistency`** uses engine method `blend_smoothed_cv_mad_v1` (see `features.json` → `sequence`).

## Quick start

1. Clone the repository.
2. Parse `walking_sample_v1/data.jsonl` — one JSON object per line.
3. Read `walking_sample_v1/features.json` for sequence aggregates (hip motion, visibility, motion consistency).
4. (Optional) Regenerate preview images:

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
- Larger “preview” packs via **Git LFS** or external download links (not raw 500+ frame dumps in git).

## Citation

If you use this sample in research or demos, please cite the repository URL:

```text
https://github.com/Alaaharoun/QualityVision-Motion-Dataset-Samples
```

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
- **Website:** your product or docs URL (optional)

## Contact

Open an issue for pilot feedback, integration questions, or licensing for full datasets.
