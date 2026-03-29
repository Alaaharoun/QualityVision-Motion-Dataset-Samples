---
license: cc-by-nc-4.0
language:
- en
tags:
- pose-estimation
- walking
- 2d-pose
- mediapipe
- motion-dataset
- quality-vision
pretty_name: QualityVision Walking Sample (compact, 2D pose)
size_categories:
- n<1K
---

# QualityVision Walking Sample (compact)

**Small** **high-quality 2D pose** clip for **walking**, exported from the [Quality Vision Motion Dataset Engine](https://github.com/Alaaharoun/QualityVision-Motion-Dataset-Samples) pipeline: **HQ frame filtering**, optional **temporal smoothing** on accepted frames, and **sequence diagnostics** in `features.json`.

For the **full 24-source bulk export** (~967 HQ frames, ~2901 merged rows, mean quality ~0.82), clone the GitHub repo and use `bulk_24_videos_6a173caf_dataset/`, or mirror [`README_HF_BULK.md`](https://github.com/Alaaharoun/QualityVision-Motion-Dataset-Samples/blob/main/README_HF_BULK.md) to a separate Hugging Face dataset via `scripts/upload_bulk_to_huggingface.ps1`.

## Files

| File | Description |
|------|-------------|
| `data.jsonl` | One JSON object per line: normalized image-space keypoints, timestamps, optional Layer 1.1 metadata. |
| `features.json` | Sequence-level aggregates (visibility, hip motion, `motion_consistency`). |
| `global_stats.json` | Job-level roll-up for this clip. |
| `manifest.json` | Export metadata (format compatible with the Motion Dataset Engine). |
| `export_quality_report.json` | Pilot-oriented quality summary. |

## Usage

```python
from datasets import load_dataset

# If you load as JSON lines:
ds = load_dataset("Alaaharoun/QualityVision-walking-sample", data_files="data.jsonl", split="train")
```

Or download raw files:

```python
from huggingface_hub import hf_hub_download
path = hf_hub_download(
    repo_id="Alaaharoun/QualityVision-walking-sample",
    filename="data.jsonl",
    repo_type="dataset",
)
```

## License

**CC BY-NC 4.0** — see repository `LICENSE` on [GitHub](https://github.com/Alaaharoun/QualityVision-Motion-Dataset-Samples). Commercial use outside NC terms requires a separate agreement.

## Citation

```bibtex
@misc{qualityvision_walking_sample,
  title = {QualityVision Walking Sample (2D Pose)},
  author = {Alaaharoun},
  howpublished = {\url{https://huggingface.co/datasets/Alaaharoun/QualityVision-walking-sample}},
  year = {2026},
}
```
